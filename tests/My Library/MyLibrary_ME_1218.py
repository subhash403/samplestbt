import stbt
from my_library import MyLibrary

def test_MyLib_ME_1218
  # Step 1: valdiate session and liveTV, add asset to Expiring Soon if none
  init()
  ensure_expiring_soon()
  # Step 2: verify that asset in MyLibrary > Expiring Soon has a reachable ADP
  MyLibrary.open().find_lane("Expiring Soon")
  press('KEY_ENTER')
  assert stbt.wait_until(lambda: stbt.match("images/vod/adp_blankspace.png")), \
  "ADP of asset in Expiring Soon not reached"
  # Step 3: verify that asset in MyLibrary > Watchlist has a reachable ADP
  MyLibrary.open().find_lane("Watchlist")
  press('KEY_ENTER')
  assert stbt.wait_until(lambda: stbt.match("images/vod/adp_blankspace.png")), \
  "ADP of asset in Watchlist not reached"
#
