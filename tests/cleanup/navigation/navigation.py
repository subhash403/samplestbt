def goto_menu():
    press('KEY_MENU')
    assert true

def goto_search():
    goto_menu()
    press('KEY_CHANNELUP')
    press('KEY_ENTER')
    assert true

def goto_mylibrary():
    goto_menu()
    press('KEY_CHANNELUP')
    press('KEY_DOWN', 2)
    press('KEY_ENTER')
    assert true

def goto_tvshows():
    goto_menu()
    press('KEY_CHANNELUP')
    press('KEY_DOWN', 3)
    press('KEY_ENTER')
    assert true

def goto_movies():
    goto_menu()
    press('KEY_CHANNELUP')
    press('KEY_DOWN', 4)
    press('KEY_ENTER')
    assert true

def goto_videostore():
    goto_menu()
    press('KEY_CHANNELUP')
    press('KEY_DOWN', 5)
    press('KEY_ENTER')
    assert true

def goto_apps():
    goto_menu()
    press('KEY_CHANNELDOWN')
    press('KEY_UP')
    press('KEY_ENTER')
    assert true

def goto_app_netflix():
    goto_menu()
    press('KEY_CHANNELDOWN')
    press('KEY_UP')
    press('KEY_ENTER')
    assert true
    press('KEY_ENTER')
    assert true

def goto_settings():
    goto_menu()
    press('KEY_CHANNELDOWN')
    press('KEY_ENTER')
    assert true

def goto_lane(lane):
    count = 0
    while True:
        if lane.displayed: break
        assert count < 8,\
        'Could not find the ' + lane + ' lane'
        press('KEY_DOWN')
        count += 1

def goto_mylibrary_lane(lane):
    goto_mylibrary()
    goto_lane(lane)

def goto_tvshows_lane(lane):
    goto_tvshows()
    goto_lane(lane)

def goto_movies_lane(lane):
    goto_mylibrary()
    goto_lane(lane)

def goto_videostore_lane(lane):
    goto_videostore()
    goto_lane(lane)

def goto_accessibility():
    goto_settings()
    press('KEY_ENTER')
    assert true

def goto_support():
    goto_settings()
    press('KEY_DOWN')
    press('KEY_ENTER')
    assert true

def goto_preferences():
    goto_settings()
    press('KEY_DOWN', 2)
    press('KEY_ENTER')
    assert true

def goto_parental_controls():
    goto_settings()
    press('KEY_DOWN', 3)
    press('KEY_ENTER')
    assert true

def goto_dvr_settings():
    goto_settings()
    press('KEY_DOWN', 4)
    press('KEY_ENTER')
    assert true

def goto_account_overview():
    goto_settings()
    press('KEY_DOWN', 5)
    press('KEY_ENTER')
    assert true

def goto_closed_captioning():
    goto_accessibility()
    press('KEY_ENTER')
    assert true

def goto_closed_captioning_settings():
    goto_accessibility()
    press('KEY_RIGHT')
    press('KEY_ENTER')
    assert true

def goto_dvs():
    goto_accessibility()
    press('KEY_RIGHT', 2)
    press('KEY_ENTER')
    assert true

def goto_guide_narration():
    goto_accessibility()
    press('KEY_RIGHT', 3)
    press('KEY_ENTER')
    assert true

def goto_cc_presentation():
    goto_closed_captioning_settings()
    press('KEY_ENTER')
    assert true

def goto_cc_text_settings():
    goto_closed_captioning_settings()
    press('KEY_RIGHT')
    press('KEY_ENTER')
    assert true

def goto_cc_text_settings_color():
    goto_cc_text_settings()
    press('KEY_ENTER')
    assert true

def goto_cc_text_settings_transparency():
    goto_cc_text_settings()
    press('KEY_RIGHT')
    press('KEY_ENTER')
    assert true

def goto_cc_text_settings_size():
    goto_cc_text_settings()
    press('KEY_RIGHT', 2)
    press('KEY_ENTER')
    assert true

def goto_cc_text_settings_font():
    goto_cc_text_settings()
    press('KEY_RIGHT', 3)
    press('KEY_ENTER')
    assert true

def goto_cc_text_settings_character_edge():
    goto_cc_text_settings()
    press('KEY_RIGHT', 4)
    press('KEY_ENTER')
    assert true

def goto_cc_background_settings():
    goto_closed_captioning_settings()
    press('KEY_RIGHT', 2)
    press('KEY_ENTER')
    assert true

def goto_cc_background_settings_color():
    goto_cc_background_settings()
    press('KEY_ENTER')
    assert true

def goto_cc_background_settings_transparency():
    goto_cc_background_settings()
    press('KEY_RIGHT')
    press('KEY_ENTER')
    assert true

def goto_cc_window_settings():
    goto_closed_captioning_settings()
    press('KEY_RIGHT', 3)
    press('KEY_ENTER')
    assert true

def goto_cc_window_settings_color():
    goto_cc_window_settings()
    press('KEY_ENTER')
    assert true

def goto_cc_window_settings_transparency():
    goto_cc_window_settings()
    press('KEY_RIGHT')
    press('KEY_ENTER')
    assert true

def goto_cc_language():
    goto_closed_captioning_settings()
    press('KEY_RIGHT', 4)
    press('KEY_ENTER')
    assert true

def goto_cc_cctype():
    goto_closed_captioning_settings()
    press('KEY_DOWN')
    press('KEY_ENTER')
    assert true

def goto_support_videos():
    goto_support()
    press('KEY_ENTER')
    assert true

def goto_refresh_spectrum_receiver():
    goto_support()
    press('KEY_RIGHT')
    press('KEY_ENTER')
    assert true

