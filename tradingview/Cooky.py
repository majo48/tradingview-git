"""
Cookies retrieved from Chrome are used for Authentication to trading-view API
Prerequisites:
1. Chrome Browser must be running an instance of tradinview.com
2. First time use: enter password and click button 'Always allow"
"""

import os
import datetime
import pathlib
from http.cookiejar import CookieJar

import rookiepy
import pickle

class Cooky:

    def __init__(self):
        """
        Initialize Cooky class
        """
        pass

    # local methods =====

    def _check_cookies(self, cookies: CookieJar):
        """
        Check for cookie pointing to tradingview.com
        :param cookies:
        :return: True is OK, False is error
        """
        for item in cookies._cookies:
            if item == '.tradingview.com':
                return True
        return False

    # public methods =====

    def get_cookies(self):
        """
        Get current cookie from Chrome Browser
        """
        cookies: CookieJar = rookiepy.to_cookiejar(rookiepy.chrome(['.tradingview.com']))
        if self._check_cookies(cookies):
            return cookies
        else:
            return None # error

if __name__ == '__main__':
    print("The Cooky class module shall not be invoked on it's own.")
