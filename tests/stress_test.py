import stbt

def test_weekend_run():
    stbt.press('KEY_EXIT')
    stbt.press('KEY_EXIT')
    stbt.press('KEY_GUIDE')
    assert stbt.wait_until(lambda: stbt.match("images/guide_options.png")), \
		"Guide not launched"
    stbt.press('KEY_4')    
    stbt.press('KEY_INFO')
    count =0
    while TRUE:
    	if stbt.wait_until(lambda: stbt.match("images/view_series_info.png")): break
    	else:
    		stbt.press('KEY_RIGHT')
    	count +=1
	if count > 10:
		assert stbt.wait_until(lambda: stbt.match("images/view_series_info.png")), \
		"Asset did not have a view series info cta"
                
    stbt.press('KEY_SELECT')            
    stbt.press('KEY_RIGHT')
    stbt.press('KEY_SELECT')
    stbt.press('KEY_OPTIONS')
