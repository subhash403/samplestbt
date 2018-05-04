def goto_menu():
    assert true

def goto_search():
    goto_menu()
    press('KEY_CHANNELUP')
    press('KEY_ENTER')
    assert true

def goto_mylibrary():
    goto_menu()
    press('KEY_CHANNELUP')
    press('KEY_DOWN','2')
    press('KEY_ENTER')
    assert true

def goto_tvshows():
    goto_menu()
    press('KEY_CHANNELUP')
    press('KEY_DOWN', '3')
    press('KEY_ENTER')
    assert true

def goto_movies():
    goto_menu()
    press('KEY_CHANNELUP')
    press('KEY_DOWN', '4')
    press('KEY_ENTER')
    assert true

def goto_videostore():
    goto_menu()
    press('KEY_CHANNELUP')
    press('KEY_DOWN', '5')
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

def find_lane(lane):
    count = 0
    while True:
        if lane.displayed: break
        assert count < 8,\
        'Could not find the ' + lane + ' lane'
        press('KEY_DOWN')
        count += 1

def goto_mylibrary_lane(lane):
    goto_mylibrary()
    find_lane(lane)

def goto_tvshows_lane(lane):
    goto_tvshows()
    find_lane(lane)

def goto_movies_lane(lane):
    goto_mylibrary()
    find_lane(lane)

def goto_videostore_lane(lane):
    goto_videostore()
    fine_lane(lane)