import stbt
import time
from datetime import datetime

def test_weekend_run():
    stbt.press('KEY_EXIT')
    stbt.press('KEY_EXIT')
    stbt.press('KEY_GUIDE')
    if stbt.wait_until(lambda: stbt.match("images/guide_filter_favorites.png")):
	stbt.press('KEY_OPTIONS')
	stbt.press('KEY_DOWN')
    	stbt.press('KEY_ENTER')
	
    assert stbt.wait_until(lambda: stbt.match("images/guide_options.png")), \
		"Guide not launched"
    stbt.press('KEY_4')   
    time.sleep(3)
    stbt.press('KEY_INFO')
	
    if stbt.wait_until(lambda: stbt.match("images/enter_pin_guide.png")):
	stbt.press('KEY_0')
	stbt.press('KEY_0')
	stbt.press('KEY_0')
	stbt.press('KEY_0')
	stbt.press('KEY_ENTER')
	
    count =0
    while True:
    	if stbt.wait_until(lambda: stbt.match("images/view_series_info.png")): break
    	stbt.press('KEY_RIGHT')
    	count +=1
	if count > 10:
		assert stbt.wait_until(lambda: stbt.match("images/view_series_info.png")), \
		"Asset did not have a view series info cta"
                
    stbt.press('KEY_ENTER')   
    if stbt.wait_until(lambda: stbt.match("images/series_info_unavailable.png"))
	print "Unable to added guide asset to the watchlist because series info unavailable was seen in the environment within the asset after selecting the view series info cta"
    stbt.press('KEY_RIGHT')
    stbt.press('KEY_ENTER')
    if stbt.wait_until(lambda: stbt.match("images/removed_from_watchlist.png")): 
		stbt.press('KEY_ENTER')
		stbt.press('KEY_ENTER')
		
    assert stbt.wait_until(lambda: stbt.match("images/added_to_watchlist.png")), \
    "Added to watchlist did not appear when selecting the cta in the guide"

    stbt.press('KEY_ENTER')
    stbt.press('KEY_LAST')
    stbt.press('KEY_LAST')
    stbt.press('KEY_OPTIONS')

    assert stbt.wait_until(lambda: stbt.match("images/guide_filters.png")), \
    "Filters not entered upon selecting options on black remote"

    stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')

    assert stbt.wait_until(lambda: stbt.match("images/guide_filter_favorites.png")), \
    "Filter not applied after selecting favorites filter from options in the guide"

    assert stbt.wait_until(lambda: stbt.match("images/heart_icons_for_filter.png")), \
    "Heart Icons not found on guide after applying favorites filter"

    stbt.press('KEY_EXIT')
    stbt.press('KEY_EXIT')
    stbt.press('KEY_GUIDE')
	
    assert stbt.wait_until(lambda: stbt.match("images/guide_filter_favorites.png")), \
    "Filter not applied after closing the guide and reopening"
	
    stbt.press('KEY_OPTIONS')	

    assert stbt.wait_until(lambda: stbt.match("images/guide_filters.png")), \
    "Filters not entered upon selecting options on black remote"

    stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
	
    assert stbt.wait_until(lambda: stbt.match("images/guide_options.png")), \
    "Filter not taken away after selecting favorites filter from options in the guide while the filter is already applied"
	
    stbt.press('KEY_4')  
    time.sleep(3)
    stbt.press('KEY_INFO')
    if stbt.wait_until(lambda: stbt.match("images/enter_pin_guide.png")):
	stbt.press('KEY_0')
	stbt.press('KEY_0')
	stbt.press('KEY_0')
	stbt.press('KEY_0')
	stbt.press('KEY_ENTER')
	
    count =0
    while True:
    	if stbt.wait_until(lambda: stbt.match("images/view_series_info.png")): break
    	stbt.press('KEY_RIGHT')
    	count +=1
	if count > 10:
		assert stbt.wait_until(lambda: stbt.match("images/view_series_info.png")), \
		"Asset did not have a view series info cta"

    stbt.press('KEY_ENTER')            
    stbt.press('KEY_RIGHT')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/removed_from_watchlist.png")), \
    "Removed to watchlist did not appear when selecting the cta in the guide"

