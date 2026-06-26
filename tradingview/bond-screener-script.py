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

# main
c = Cooky()
cookies = c.get_cookies()
if cookies is None:
    print('Please open Chrome Browser and login to tradingview.com.')
    sys.exit(1) # error

print(cookies)

# ====
# Close script
sys.exit(0) # finished