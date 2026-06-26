#!/bin/sh
"""
Get a list of bonds using the tradingview.com API
Policy for Queries:
    - always authorized with cookies
    - less than one query per minute
    - max 50 lines (limit result)
"""
import sys
from Cooky import Cooky
from Timer import Timer

# main ===
c = Cooky()
cookies = c.get_cookies()
if cookies is None:
    print('Please open Chrome Browser and login to tradingview.com.')
    sys.exit(1) # error
print(cookies)

t = Timer()
OK = t.check_timelapse()
if not OK:
    print('Please wait a bit longer for the next query to tradingview.com.')
    sys.exit(2) # error

print('Add query here.')

# ====
# Close script
sys.exit(0) # finished