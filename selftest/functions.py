'''
# Test functions

The functions in this module are meant to test individual
components of an AstroPi flight unit.

All test functions:
- Return either True or False, depending on whether the test
  has been successful or not.
- May raise exceptions if a test cannot be performed.
- Use logger.debug() to display additional test-related information

Here is a list of all the tests on offer:

- detect_sensehat()
- test_cputemp()
- test_voltage()
- test_throttled()
- test_astropi_gpio()
- test_camera()
- test_temperature
- test_pressure
- test_humidity         [interactive]
- test_gyroscope        [interactive]
- test_accelerometer    [interactive]
- test_magnetometer     [interactive]
#- test_tcs34725        [interactive]
- test_joystick         [interactive]
- test_buttons          [interactive]
- test_motion           [interactive]
'''

import os
import io
import re
import subprocess
from time import sleep, monotonic
from logzero import logger
from select import select
from math import sqrt
from functools import partial

from sense_hat import SenseHat
from picamera import PiCamera
from gpiozero import MotionSensor, Button
from gpiozero.pins.rpigpio import RPiGPIOFactory
pin_factory = RPiGPIOFactory() # NativeFactory has issues on Pi 4
import evdev

'''
# Support for the TCS34725 sensor on the new Sense HAT
from tcs34725 import TCS34725
'''

wait_colour = (255,0,0)
pass_colour = (0,255,0)

# how long to wait after an interactive test
POST_TEST_DELAY = 1


# helper functions

def is_pi4():
    '''
    Return True if this is running on a Pi 4 (by reading `/proc/device-tree/model`),
    or False otherwise
    '''
    with open('/proc/device-tree/model') as model:
        result = 'Raspberry Pi 4' in model.read()
    return result

def test_i2c_address(address, bus=1):
    """
    Return True if a device is present on a specific `address` 
    on the I2C `bus`, and False otherwise. 
    """
    assert bus in (0, 1)
    if not os.path.isdir(f'/sys/bus/i2c/devices/{bus}-00{address}'):
        logger.debug(f'test_i2c_address: Failed to detect device at 0x{address} (bus {bus})')
        return False
    return True

def vcgencmd(args, regexp):
    '''
    Run `vcgencmd` using `args` as arguments, then match the output
    against a regular expression and return the matched group(s).
    '''
    output = subprocess.run(['vcgencmd'] + args, capture_output=True, text=True).stdout.strip()
    match = regexp.match(output)
    if match is None:
        return None
    result = match.groups()
    if len(result) == 1:
        result = result[0]
    return result

# Regular expressions to parse the output of `vcgencmd`
camera_output = re.compile('supported=([01]) detected=([01])')
temp_output = re.compile('temp=([0-9]*\.[0-9])\'C')
voltage_output = re.compile('volt=([0-9]*\.[0-9]*)V')
throttled_output = re.compile('throttled=(0x[0-9a-fA-F]{1,5})')

def test_vcgencmd(command, regexp, test_function):
    '''
    Run a `vcgencmd` command, then match the output against
    a regular expression and run a test function on the
    matched group(s).
    '''
    result = vcgencmd([command], regexp)
    assert result is not None
    logger.debug(f'test_vcgencmd: `vcgencmd {command}` output is {result}')
    return test_function(result)

def average(function, time, polling):
    """
    Call `function` at regular `polling` intervals, for a specific amount
    of `time` and return the average value.

    Useful for polling a sensor and returning an average over some time.
    """
    # disregard the first 3 readings
    # (some sensors may generate spurious values at startup)
    for _ in range(3):
        sleep(polling)
        function()
    s = 0
    n = int(time//polling) if time > polling else 1
    for _ in range(n):
        sleep(polling)
        value = function()
        s += value
    return s/n

def maximum(function, time, polling):
    """
    Call `function` at regular `polling` intervals, for a specific amount
    of `time` and return the maximum value.

    Useful for polling a sensor and returning a maximum over some time.
    """
    # disregard the first 3 readings
    # (some sensors may generate spurious values at startup)
    for _ in range(3):
        sleep(polling)
        function()
    # get initial max value
    sleep(polling)
    m = function()
    n = int(time//polling)
    for _ in range(n):
        sleep(polling)
        value = function()
        if value > m:
            value = m 
    return m

def in_range(value, low=None, high=None):
    """
    Return True if `value` is greater than `low` and lower than `high`,
    or False otherwise. If any of `low` or `high` is None, then there
    is no corresponding condition.
    """
    return (
        (low is None or value >= low) and 
        (high is None or value <= high)
    )

def display(sensehat, coords, colour):
    for x, y in coords:
        sensehat.set_pixel(x, y, colour)


# CPU temperature test

def get_cputemp():
    return float(vcgencmd(['measure_temp'], temp_output))

def test_cputemp():
    '''
    Return True if the CPU temperature, as reported by `vcgencmd measure_temp`,
    is within safe levels, or False otherwise.
    '''
    # https://www.raspberrypi.org/documentation/hardware/raspberrypi/frequency-management.md
    return test_vcgencmd('measure_temp', temp_output, lambda result: float(result) < 80)


# Voltage and under-voltage tests

def test_voltage():
    """
    Return True if the voltage (as reported by `vcgencmd measure_volts`)
    is within a nominal range, or False otherwise.
    On models before the Pi 4, the nominal voltage value is 1.2V. On the 
    Pi 4, the voltage is determined dynamically, depending on load.
    """
    if is_pi4():
        return test_vcgencmd(
            'measure_volts', voltage_output, 
            lambda result: 0.825 <= float(result) < 1.25
        )
    else:
        return test_vcgencmd(
            'measure_volts', voltage_output, 
            lambda result: abs(float(result) - 1.2) < 0.01
        )

# https://www.raspberrypi.org/documentation/raspbian/applications/vcgencmd.md
throttled_map = {
    0x1:     "Under-voltage detected",
    0x2:     "Arm frequency capped",
    0x4:	 "Currently throttled",
	0x8:	 "Soft temperature limit active",
	0x10000: "Under-voltage has occurred",
	0x20000: "Arm frequency capping has occurred",
	0x40000: "Throttling has occurred",
    0x80000: "Soft temperature limit has occurred"
}

def vcgencmd_throttled():
    '''
    Retrieve the output of `vcgencmd get_throttled`, which is 
    a bit pattern. Use the hex values in the `throttled_map` dict
    as masks to break down the bit pattern and return a list of
    the hex values for which the corresponding bit is set.
    '''
    result = vcgencmd(['get_throttled'], throttled_output)
    assert result is not None
    pattern = int(result, 16)
    return [mask for mask in throttled_map if pattern & mask > 0]
    
def test_throttled():
    '''
    Return True if the output of `vcgencmd get_throttled` indicates an
    undervoltage event (either currently or since boot), or False otherwise.
    '''
    flags = vcgencmd_throttled()
    for flag in flags:
        logger.debug(f'test_throttled: {throttled_map[flag]}')
    return not any(flag in flags for flag in (0x1, 0x10000))


# camera test

def test_camera_vcgencmd():
    '''
    Return True if the Pi camera is detected and enabled 
    (as reported by `vcgencmd get_camera`), or False otherwise.
    '''
    return test_vcgencmd(
        'get_camera', camera_output, 
        lambda result: all(value=='1' for value in result)
    )

def test_camera(filename=None):
    '''
    Return True if the Pi camera is detected, enabled and 
    is able to capture data, or False otherwise.
    Save the image data to `filename`, if it is not None.
    '''
    if not test_camera_vcgencmd():
        return False
    if filename:
        stream = open(filename, 'wb')
    else:
        stream = io.BytesIO()
    with PiCamera() as camera:
        camera.capture(stream, 'jpeg')
    result = bool(stream.tell())
    stream.close()
    return result


# Sense Hat tests

def detect_sensehat():
    '''
    Return a SenseHAT object, if it can be created, or None otherwise.
    '''
    try:
        return SenseHat()
    except Exception as e:
        logger.debug(f'check_sensehat: {e.__class__.__name__}: {e}')
        return None

def test_temperature_bounds(sensehat, time=1, polling=0.1, reasonable_min=None, reasonable_max=None):
    """
    Return True if the average Sense HAT temperature reading over a `time` interval
    is within within "reasonable" range (i.e. between `reasonable_min` and `reasonable_max`),
    or False otherwise.
    """
    if not test_i2c_address('5c') or not test_i2c_address('5f'):
        return False
    temperature = average(sensehat.get_temperature, time, polling)
    min_str = reasonable_min if reasonable_min is not None else ''
    max_str = reasonable_max if reasonable_max is not None else ''
    logger.debug(f'test_temperature: Temperature reading is {temperature} {min_str}->{max_str}')
    return in_range(temperature, reasonable_min, reasonable_max)

def test_temperature(sensehat, time=1, polling=0.1):
    """
    Return True if the average Sense HAT temperature reading over a `time` interval
    is between 10 degrees and the CPU temperature.
    """
    return test_temperature_bounds(sensehat, time, polling, reasonable_min=10, reasonable_max=get_cputemp())

def test_humidity(sensehat, timeout=None, time=1, polling=0.1):
    """
    If the `timeout` is None:
    Return True if the average Sense HAT humidity reading over a `time` interval
    is between 0 and 100, or False otherwise.
    If the `timeout` is not None, the test is interactive: 
    Return True if a Sense HAT humidity reading that exceeds a threshold is 
    input within `timeout` seconds, or False otherwise.
    The threshold is the initial average Sense HAT humidity reading 
    over a `time` interval plus 2.
    """
    if not test_i2c_address('5f'):
        return False
    humidity = average(sensehat.get_humidity, time, polling)
    logger.debug(f'test_humidity: Humidity reading is {humidity}')
    if timeout is None:
        return 0 < humidity <= 100
    
    # interactive
    center = [(3,2), (4,2), 
              (2,3), (5,3),
              (2,4), (5,4),
              (3,5), (4,5),
             ]
    sensehat.clear()
    display(sensehat, center, wait_colour)

    threshold = humidity + 2.0

    start = monotonic()
    print(f'test_humidity: Breathe on the Astro Pi (timeout: {timeout} secs)')
    while monotonic() - start < timeout:
        sleep(polling)
        value = sensehat.get_humidity()
        if value >= threshold:
            display(sensehat, center, pass_colour)
            sleep(POST_TEST_DELAY)
            return True
    return False

def test_pressure_bounds(sensehat, time=1, polling=0.1, reasonable_min=None, reasonable_max=None):
    """
    Return True if the average Sense HAT pressure reading over a `time` interval
    is within within "reasonable" range (i.e. between `reasonable_min` and `reasonable_max`),
    or False otherwise.
    """
    if not test_i2c_address('5c'):
        return False
    min_str = reasonable_min if reasonable_min is not None else ''
    max_str = reasonable_max if reasonable_max is not None else ''
    pressure = average(sensehat.get_pressure, time, polling)
    logger.debug(f'test_pressure: Pressure reading is {pressure} {min_str}->{max_str}')
    return pressure > 0 and in_range(pressure, reasonable_min, reasonable_max)

def test_pressure(sensehat, time=1, polling=0.1):
    """
    Return True if the average Sense HAT pressure reading over a `time` interval
    is between 800 and 1200 millibars.
    """
    return test_pressure_bounds(
        sensehat, time, polling,
        reasonable_min=800, reasonable_max=1200
    )

def test_gyroscope(sensehat, timeout=None, polling=0.1):
    """
    If the `timeout` is None:
    Return True if the Sense HAT gyroscope readings for 'pitch', 'roll' and 'yaw'
    are all between 0 and 360, or False otherwise.
    If the `timeout` is not None, the test is interactive: 
    Return True if the SenseHAT is tilted up, down, left and right by 30 degrees
    within `timeout` seconds, or False otherwise.
    """
    if not test_i2c_address('1c') or not test_i2c_address('6a'):
        return False
    gyroscope = sensehat.gyroscope
    logger.debug(f'test_gyroscope: gyroscope reading is {gyroscope}')
    if timeout is None:
        return all(0 <= gyroscope[axis] <= 360 for axis in ('pitch', 'roll', 'yaw'))

    # interactive
    dirmap = {
        'up': [(3,1), (4,1), (3,2), (4,2)],
        'down': [(3,5), (4,5), (3,6), (4,6)],
        'left': [(1,3), (1,4), (2,3), (2,4)],
        'right': [(5,3), (5,4), (6,3), (6,4)],
    }   
    sensehat.clear()
    for direction in dirmap:
        display(sensehat, dirmap[direction], wait_colour)

    directions = set(dirmap.keys())
    start = monotonic()
    print(f'test_gyroscope: Tilt the Astro Pi left, right, up and down, in any order (timeout: {timeout} secs)')
    while monotonic() - start < timeout:
        sleep(polling)
        direction = None
        pitch = 180-sensehat.gyroscope['pitch']
        roll = 180-sensehat.gyroscope['roll']
        if 0 < pitch <= 150:
            direction = 'up'
        elif 0 > pitch >= -150:
            direction = 'down'
        if 0 < roll <= 150:
            direction = 'left'
        elif 0 > roll >= -150:
            direction = 'right'
        if direction is not None and direction in directions:
            display(sensehat, dirmap[direction], pass_colour)
            directions.remove(direction)
            if not directions:
                sleep(POST_TEST_DELAY)
                return True
    return False
    
def test_accelerometer(sensehat, timeout=None, polling=0.1):
    """
    If the `timeout` is None:
    Return True if the Sense HAT raw accelerometer readings for 'x', 'y' and 'z'
    are all less than 1.2 in absolute value, or False otherwise.
    If the `timeout` is not None, the test is interactive: 
    Return True if the SenseHAT detects a combined acceleration exceeding 1.5 g's
    within `timeout` seconds, or False otherwise.
    """
    if not test_i2c_address('1c') or not test_i2c_address('6a'):
        return False
    accelerometer = sensehat.get_accelerometer_raw()
    logger.debug(f'test_accelerometer: accelerometer reading is {accelerometer}')
    if timeout is None:
        return all(abs(accelerometer[axis]) < 1.2 for axis in ('x', 'y', 'z'))

    # interactive
    g = [
        (4,1), (5,1), (6,1),
        (6,2),
        (6,3),
        (1,4),
        (1,5),
        (1,6), (2,6), (3,6)
    ]
    sensehat.clear()
    display(sensehat, g, wait_colour) 

    threshold = 1.5
    start = monotonic()
    print(f'test_accelerometer: Shake the Astro Pi (timeout: {timeout} secs)')
    while monotonic() - start < timeout:
        sleep(polling)
        accelerometer = sensehat.get_accelerometer_raw()
        value = sqrt(sum(accelerometer[axis]**2 for axis in ('x', 'y', 'z')))
        if value >= threshold:
            display(sensehat, g, pass_colour)
            sleep(POST_TEST_DELAY)
            return True
    return False

def test_magnetometer(sensehat, timeout=None, time=1, polling=0.1):
    """
    If the `timeout` is None:
    Return True if the average Sense HAT compass readings over a `time` interval`
    are between 0 and 360, or False otherwise.
    If the `timeout` is not None, the test is interactive: 
    Return True if the SenseHAT detects a deviation of 60 degrees from the initial
    average compass reading within `timeout` seconds, or False otherwise.
    """
    if not test_i2c_address('1c') or not test_i2c_address('6a'):
        return False
    compass = average(sensehat.get_compass, time, polling)
    logger.debug(f'test_magnetometer: compass reading is {compass}')
    if timeout is None:
        return in_range(compass, 0.0, 360.0)

    # interactive
    slash = [(2,2), (3,3), (4,4), (5,5)]
    sensehat.clear()
    display(sensehat, slash, wait_colour)

    start = monotonic()
    print(f'test_magnetometer: Rotate the Astro Pi to change direction (time: {timeout} secs)')
    while monotonic() - start < timeout:
        sleep(polling)
        value = sensehat.get_compass()
        if abs(value - compass) >= 60:
            display(sensehat, slash, pass_colour)
            sleep(POST_TEST_DELAY)
            return True
    return False


# evdev-based tests

# https://python-evdev.readthedocs.io/en/latest/usage.html
def get_evdev_device(name):
    '''
    Return an evdev device with a given name, if it exists.
    '''
    for path in evdev.list_devices():
        device = evdev.InputDevice(path)
        if device.name == name:
            return device
    return None

def test_evdev_device(name, keys=None, timeout=None, sensehat=None, keymap=None):
    """
    If the `timeout` is None:
    Return True if an evdev device with a particular `name` exists, 
    or False otherwise.
    If the `timeout` is not None, the test is interactive: 
    Return True if all the `keys` are pressed within `timeout` seconds,
    or False otherwise.
    If a `senseHat` is present, then the `keymap` is used to map the `keys`
    to indicators on the LED matrix.
    """
    device = get_evdev_device(name)
    if device is None:
        logger.debug(f'test_evdev_device: Failed to detect evdevice {name}')
        return False
    if keys is None or timeout is None:
        return True
    
    if sensehat:
        sensehat.clear()
        for key in keys:
            display(sensehat, keymap[key], wait_colour)

    device.grab()
    # test for events using a timeout
    # https://github.com/gvalkov/python-evdev/issues/33
    poll = 0.1
    #print(f'{name}: {", ".join(keys)} ({timeout} secs)')
    keys = set(keys)
    nb_keys = len(keys)
    for _ in range(int(timeout/poll)):
        if select([device], [], [], poll)[0]:
            for event in device.read():
                if event.type == evdev.ecodes.EV_KEY:
                    key = evdev.ecodes.KEY[event.code]
                    if key in keys:
                        #print(key)
                        if sensehat:
                            display(sensehat, keymap[key], pass_colour)
                        keys.remove(key)
                        if not keys:
                            device.ungrab()
                            sleep(POST_TEST_DELAY)
                            return True
    
    device.ungrab()
    if sensehat:
        sensehat.clear()
    return False

def test_joystick(sensehat, timeout=None):
    if timeout is not None:
        print(f'test_joystick: Move the joystick left, right, up and down and press its button, in any order (timeout: {timeout} secs)')
    keymap = {
        'KEY_LEFT': [(3,0), (4,0), (3,1), (4,1)],
        'KEY_RIGHT': [(3,6), (4,6), (3,7), (4,7)],
        'KEY_DOWN': [(0,3), (0,4), (1,3), (1,4)],
        'KEY_UP': [(6,3), (6,4), (7,3), (7,4)],
        'KEY_ENTER': [(3,3), (3,4), (4,3), (4,4)]
    }
    return test_evdev_device(
        'Raspberry Pi Sense HAT Joystick', 
        ['KEY_UP', 'KEY_DOWN', 'KEY_LEFT', 'KEY_RIGHT', 'KEY_ENTER'],
        timeout, sensehat, keymap
    )

def test_buttons(sensehat, timeout=None, polling=0.1):
    if timeout is None:
        print(f'test_buttons: Buttons can only be tested in interactive mode')
        return False        

    print(f'test_buttons: Press buttons A and B, in any order (timeout: {timeout} secs)')
    keymap = {
        'KEY_A': [(1,3), (1,4), (2,3), (2,4)],
        'KEY_B': [(5,3), (5,4), (6,3), (6,4)],
    }

    sensehat.clear()
    for key in keymap:
        display(sensehat, keymap[key], wait_colour)

    keys = set(keymap.keys())

    def handle(key):
        display(sensehat, keymap[key], pass_colour)
        keys.remove(key)

    def handler_a():
        handle('KEY_A')

    def handler_b():
        handle('KEY_B')

    button_A = Button(20)
    button_A.when_pressed = handler_a
    button_B = Button(21)
    button_B.when_pressed = handler_b

    start = monotonic()
    while monotonic() - start < timeout and keys:
        sleep(polling)

    if not keys:
        sleep(POST_TEST_DELAY)
        return True
    else:
        return False

# gpiozero-based tests

def test_motion_pin(pin_number, timeout=None, sensehat=None):
    """
    If the `timeout` is None:
    Return True if a `MotionSensor` object can be created on `pin_number`,
    or False otherwise
    If the `timeout` is not None, the test is interactive: 
    Return True if motion can be detected by the MotionSensor 
    within `timeout` seconds.
    If a `senseHat` is present, then an indicator is displayed on the LED matrix.
    """
    pir = MotionSensor(pin_number)
    if timeout is None:
        return True
    
    # interactive
    if sensehat is not None:
        center = [(3,3), (3,4), (4,3), (4,4)]
        sensehat.clear()
        display(sensehat, center, wait_colour)

    print(f'test_motion: Move any object around the Astro Pi (timeout: {timeout} secs)')
    motion = pir.wait_for_motion(timeout)

    if motion and sensehat is not None:
        display(sensehat, center, pass_colour)
        sleep(POST_TEST_DELAY)

    return motion

def test_motion(sensehat, timeout=None):
    return test_motion_pin(26, timeout, sensehat)

def test_gpiopin(pin_number, tests):
    """
    Return True if the `tests` performed on GPIO `pin_number` are all successful.
    - A 'write' test sets a pin as an output pin and checks to see if write 0 
      and write 1 are successful.
    - A 'pull-up' test sets a pin as a pulled-down input pin and checks if
      it's state is 1.
    - A 'pull-down' test sets a pin as a pulled-up input pin and checks if
      it's state is 0.

    These tests largely follow the test patterns from pigpio's gpiotest and
    the gpiozero's test_real_pins:

    http://abyz.me.uk/rpi/pigpio/code/gpiotest.zip
    https://github.com/gpiozero/gpiozero/blob/master/tests/test_real_pins.py
    """
    pin = pin_factory.pin(pin_number)

    # record current pin state, in order to restore later
    if pin.function == 'input':
        saved = (pin.function, pin.pull)
    else:
        saved = (pin.function, pin.state)
    successful = True

    if 'write' in tests:
        pin.function = 'output'
        pin.state = 1
        if pin.state != 1:
            logger.debug(f"test_gpiopin: Write 1 to {pin} failed.")
            successful = False
        pin.state = 0
        if pin.state != 0:
            logger.debug(f"test_gpiopin: Write 0 to {pin} failed.")
            successful = False

    if 'pull-up' in tests:
        pin.function = 'input'
        try:
            pin.pull = 'up'
            if pin.state != 1:
                logger.debug(f"Pull-up on {pin} failed.")
                successful = False
        except Exception as e:
                logger.debug(f"Pull-up on {pin} failed. {e.__class__.__name__}: {e}")
                successful = False

    if 'pull-down' in tests:
        pin.function = 'input'
        try:
            pin.pull = 'down'
            if pin.state != 0:
                logger.debug(f"Pull-down on {pin} failed.")
                successful = False
        except Exception as e:
                logger.debug(f"Pull-down on {pin} failed. {e.__class__.__name__}: {e}")
                successful = False

    # restore initial pin state
    if saved[0] == 'input':
        pin.function, pin.pull = saved
    else:
        pin.function, pin.state = saved

    pin.close()
    return successful

def test_astropi_gpio():
    '''
    Return True if the GPIO pins on the Astro Pi are successfully tested
    and False otherwise.

    (see Astro Pi schematics)
    - Pins 2, 3, 23, 24, 25 and 8 are used by the sensehat HAT (no tests performed)
      (source: https://pinout.xyz/pinout/sensehat_hat)
    - Pins 13, 16, 19, 20, 21, 26 are used by buttons. Pull-downs will fail on these pins.
    - Pin 12 is used by the PIR sensor on the Pi 4
    '''
    if is_pi4():
        successful = all(
            test_gpiopin(pin, 'write, pull-down, pull-up')
               for pin in (4, 5, 6, 7, 9, 10, 11, 14, 15, 17, 18, 22))
    else:
        successful = all(
            test_gpiopin(pin, 'write, pull-down, pull-up')
            for pin in (4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 17, 18, 22, 27))

    return successful
