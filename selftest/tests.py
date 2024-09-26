from logzero import logger
from functools import partial


class Test:
    """
    A Test wraps itself around a test function and offers a unified
    approach to running the test (calling the function) and reporting
    on its results.
    """

    # a class instance of the SenseHat, to report results on the LEDs 
    sensehat = None

    # the colours used to report results
    colours = {
        'pre': (255,255,0),     # while the test is running 
        'result': {
            True: (0,255,0),    # Passed
            False: (0,255,255), # Failed
        },
        'error': (255,0,0),     # Other sort of error (e.g. an exception)
    }

    def __init__(self, test_function, led=None, timeout=None, requires_sensehat=False):
        """
        Associate an instance of the Test class with the `test_function`.
        """
        self.test = test_function
        self.led = led
        self.timeout = timeout
        if self.timeout:
            self.restorable()
        self.requires_sensehat = requires_sensehat

    def _call(self):
        if self.requires_sensehat:
            if self.timeout is None:
                return self.test(self.sensehat)
            else:
                return self.test(self.sensehat, timeout=self.timeout)
        else:
            if self.timeout is None:
                return self.test()
            else:
                return self.test(self.timeout)

    def report_pre(self):
        if self.sensehat:
            self.sensehat.set_pixel(self.led % 8, self.led // 8, self.colours['pre'])

    def report_result(self, result):
        if self.sensehat:
            self.sensehat.set_pixel(self.led % 8, self.led // 8, self.colours['result'][result])
        result = 'PASS' if result else 'FAIL'
        logger.info(f'{self.test.__name__}: {result}')

    def report_error(self, exception):
        if self.sensehat:
            self.sensehat.set_pixel(self.led % 8, self.led // 8, self.colours['error'])
        logger.error(f'{self.test.__name__}: ERROR - {exception.__class__.__name__}: {exception}')

    def run(self):
        self.report_pre()
        try:
            result = self._call()
        except Exception as e:
            self.report_error(e)
        else:
            self.report_result(result)
            return result

    def _restorable_call(self, sensehat):
        # save current matrix state, in order to restore later
        state = sensehat.get_pixels()
        # perform test
        result = self._core_call()
        # restore initial matrix state
        sensehat.set_pixels(state)
        return result

    def restorable(self):
        """
        Indicate that the Test makes use of the Sense HAT LED Matrix
        and make sure that the initial state of the LED Matrix is 
        restored after the Test has been performed. 
        """
        self._core_call = self._call
        self._call = partial(self._restorable_call, self.sensehat)
