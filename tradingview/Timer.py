"""
Timer which assures that queries to tradingview.com respect a minimal lapse of one minute.
"""

import os
import datetime
import pathlib
import pickle

MIN_LAPSE = 60 # seconds

class Timer:

    def __init__(self):
        """
        Initialize Timer class
        """
        root = pathlib.Path(__file__).parent
        self.filename = os.path.join(root, 'timer.pkl')

    # local methods

    def _set_pickled_timer(self, now):
        """
        Persist current time object to file
        :param now:
        :return: True = success, False = failed
        """
        try:
            if os.path.exists(self.filename):
                os.remove(self.filename)
            with open(self.filename, 'wb') as f:
                pickle.dump(now, f)
            return True
        except IOError as err:
            print(err)
        return False

    def _get_lapsed_secs(self, now):
        """
        Calculate how much time has lapsed since previous query
        :param now:
        :return: time in seconds
        """
        if os.path.exists(self.filename):
            t = pickle.load(open(self.filename, 'rb'))
            diff = now - t
            secs = diff.total_seconds()
            return int(secs)
        else:
            return 60 * 60 * 24 # one days worth of seconds

    # public methods

    def check_timelapse(self):
        """
        Check to see if one minute has passed since last query
        :return: True = Yes, False = No
        """
        now = datetime.datetime.now()
        lapse = self._get_lapsed_secs(now)
        if lapse > MIN_LAPSE:
            return self._set_pickled_timer(now) # please proceed if True
        else:
            return False # please wait a bit longer
