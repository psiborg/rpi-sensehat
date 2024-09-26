import argparse
import logging
from logzero import loglevel

from tests import Test
from functions import *

if __name__ == '__main__':

    # parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-v", "--verbose", action='store_true',
        help="Include debugging messages in log")
    parser.add_argument(
        "--timeout", metavar='secs', default=None, type=int,
        help="Run interactive test versions which fail after this timeout")
    args = parser.parse_args()
    loglevel(logging.INFO if not args.verbose else logging.DEBUG)

    # check for a sensehat
    sensehat = Test(detect_sensehat).run()
    if sensehat:
        sensehat.clear()
        sensehat.set_rotation(270)
        Test.sensehat = sensehat
    else:
        logger.error('SenseHat not detected')
        exit(1)

    # create the tests
    tests = [
        Test(test_cputemp, 0),
        Test(test_voltage, 1),
        Test(test_throttled, 2),
        Test(test_astropi_gpio, 3),
        Test(test_camera, 8),
        Test(test_temperature, 16, requires_sensehat=True),
        Test(test_pressure, 17, requires_sensehat=True),
        Test(test_humidity, 18, args.timeout, requires_sensehat=True),
        Test(test_gyroscope, 19, args.timeout, requires_sensehat=True),
        Test(test_accelerometer, 20, args.timeout, requires_sensehat=True),
        Test(test_magnetometer, 21, requires_sensehat=True),
        Test(test_motion,24,args.timeout, requires_sensehat=True)
        #Test(test_joystick, 24, args.timeout, requires_sensehat=True),
    ]
    if args.timeout:
        tests.append(
            Test(test_buttons, 25, args.timeout, requires_sensehat=True))


    # perform the tests
    for test in tests:
        test.run()
    
