from api_test import GNarration_setting
from time import sleep
from stbt import wait_until
from my_library import MyLibrary
from video_store import Asset, VideoStore
from dialogs import UnableToPlayDialog

def test_press():
    stbt.press('KEY_MENU')

def settings_launch():
    menu_launch()
    stbt.press('KEY_CHANNELDOWN')
    stbt.press('KEY_ENTER')
    assert stbt.wait_until(lambda: stbt.match("images/menu/settings_logo.png")), \
    "Settings not launched"

def enter_pin():
    for _ in " "*4: stbt.press('KEY_0')
    stbt.press('KEY_ENTER')

def test_DVR_after_changing_settings():
    for _ in " "*3: stbt.press('KEY_EXIT')
    sleep(1)
    count1 = 1
    for _ in " "*10:
        count1 += 1
        settings_launch()
        for _ in " "*3: stbt.press('KEY_DOWN')
        for _ in " "*2: stbt.press('KEY_ENTER')
        sleep(1)
        for _ in " "*2: stbt.press('KEY_RIGHT')
        stbt.press('KEY_ENTER')
    sleep(2)
    enter_pin()
    if count1 % 2 == 0:
        stbt.press('KEY_UP')
        stbt.press('KEY_ENTER')
        for _ in " "*2: stbt.press('KEY_DOWN')
        stbt.press('KEY_ENTER')
    else:
        stbt.press('KEY_UP')
        stbt.press('KEY_DOWN')
        stbt.press('KEY_ENTER')
        stbt.press('KEY_DOWN')
        stbt.press('KEY_ENTER')
    stbt.press('KEY_RIGHT')
    stbt.press('KEY_ENTER')
    sleep(2)
    enter_pin()
    for _ in " "*2: stbt.press('KEY_RIGHT')
    stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    stbt.press('KEY_LEFT')
    stbt.press('KEY_ENTER')
    stbt.press('KEY_RIGHT')
    stbt.press('KEY_ENTER')
    stbt.press('KEY_RIGHT')
    stbt.press('KEY_ENTER')
    sleep(2)
    enter_pin()
    stbt.press('KEY_RIGHT')
    stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    stbt.press('KEY_LEFT')
    stbt.press('KEY_DOWN')
    stbt.press('KEY_ENTER')
    stbt.press('KEY_RIGHT')
    stbt.press('KEY_ENTER')
    mydvr_launch()
    count = 0
    while True:
        stbt.press('KEY_ENTER')
        sleep(1)
        if stbt.match('images/cta/watch.png') or stbt.match('images/cta/resume.png'): break
        count += 1
        assert count < 16, \
        "Could not find recording to play in DVR page"
        sleep(2)
    stbt.press('KEY_ENTER')
    sleep(3)
    assert stbt.wait_for_motion(timeout_secs=30)

def mydvr_launch():
    for _ in " "*3: stbt.press('KEY_EXIT')
    sleep(1)
    stbt.press('KEY_MYDVR')
    assert stbt.wait_until(lambda: stbt.match("images/dvr/my_dvr.png")), \
    "MyDVR not launched"
    
def test_modify_DVR_options_10plus_times():
    counter = 1
    for _ in " "*3: stbt.press('KEY_EXIT')
    sleep(5)
    stbt.press('KEY_RECORD')
    sleep(2)
    for _ in range(10):
        for _ in " "*2: stbt.press('KEY_EXIT')
        sleep(2)
        stbt.press('KEY_RECORD')
        if not stbt.wait_until(lambda: stbt.match("images/dvr/edit_ep_rec.png")) and not stbt.wait_until(lambda: stbt.match("images/dvr/edit_ep_deleted.png")):
            for _ in " "*2: stbt.press('KEY_EXIT')
            sleep(2)
            stbt.press('KEY_RECORD')
        if counter == 1 and stbt.wait_until(lambda: stbt.match("images/dvr/edit_ep_deleted.png")):
            stbt.press('KEY_RIGHT')
            stbt.press('KEY_UP')
            for _ in " "*3: stbt.press('KEY_LEFT')
            stbt.press('KEY_ENTER')
        sleep(2)
        counter += 1
        if counter%2 == 0:
            stbt.press('KEY_RIGHT')
            assert stbt.wait_until(lambda: stbt.match("images/dvr/edit_ep_deleted.png")), \
        "Cannot edit recording setting"
            stbt.press('KEY_UP')
            for _ in " "*3: stbt.press('KEY_LEFT')
            stbt.press('KEY_ENTER')
        else:
            stbt.press('KEY_RIGHT')
            assert stbt.wait_until(lambda: stbt.match("images/dvr/edit_ep_rec.png")), \
        "Cannot edit recording setting"
            stbt.press('KEY_UP')
            for _ in " "*3: stbt.press('KEY_LEFT')
            stbt.press('KEY_ENTER')
            
def test_modify_DVR_from_miniG_50plus_times():
    counter = 1
    for _ in " "*3: stbt.press('KEY_EXIT')
    sleep(5)
    stbt.press('KEY_RECORD')
    sleep(2)
    for _ in range(50):
        for _ in " "*2: stbt.press('KEY_EXIT')
        sleep(3)
        for _ in " "*2: stbt.press('KEY_ENTER')
        sleep(1)
        stbt.press('KEY_RECORD')
        if not stbt.wait_until(lambda: stbt.match("images/dvr/edit_ep_rec.png")) and not stbt.wait_until(lambda: stbt.match("images/dvr/edit_ep_deleted.png")):
            stbt.press('KEY_RECORD')
        if counter == 1 and stbt.wait_until(lambda: stbt.match("images/dvr/edit_ep_deleted.png")):
            stbt.press('KEY_RIGHT')
            stbt.press('KEY_UP')
            for _ in " "*3: stbt.press('KEY_LEFT')
            stbt.press('KEY_ENTER')
        sleep(2)
        counter += 1
        if counter%2 == 0:
            stbt.press('KEY_RIGHT')
            assert stbt.wait_until(lambda: stbt.match("images/dvr/edit_ep_deleted.png")), \
        "Cannot edit recording setting"
            stbt.press('KEY_UP')
            for _ in " "*3: stbt.press('KEY_LEFT')
            stbt.press('KEY_ENTER')
        else:
            stbt.press('KEY_RIGHT')
            assert stbt.wait_until(lambda: stbt.match("images/dvr/edit_ep_rec.png")), \
        "Cannot edit recording setting"
            stbt.press('KEY_UP')
            for _ in " "*3: stbt.press('KEY_LEFT')
            stbt.press('KEY_ENTER')
            
def test_tuning_channels_5_times():
    for _ in " "*3: stbt.press('KEY_EXIT')
    if not stbt.wait_until(lambda: stbt.match("images/env/do_you_want_to_upgrade.png")) and not stbt.wait_until(lambda: stbt.match("images/env/channel_unavailable.png")) and not stbt.wait_until(lambda: stbt.match("images/env/title_blocked.png")):
        assert stbt.wait_until(lambda: stbt.wait_for_motion()), \
    "Live TV not reached at test start"
    channels = [25,31,27,29,30]
    t = 0
    for ch in channels:
        t += 1
        for x in list(str(ch)): 
            stbt.press("KEY_" + x)
            sleep(0.6)
        sleep(4)
        if stbt.match('images/dvr/continue_to_miniguide.png') and t == 1: 
            for _ in " "*2: stbt.press('KEY_RIGHT')
            for _ in " "*2: stbt.press('KEY_ENTER')
            stbt.press('KEY_RIGHT')
            stbt.press('KEY_ENTER')
        print (t)
        sleep(20)
        if not stbt.wait_until(lambda: stbt.match("images/env/do_you_want_to_upgrade.png")) and not stbt.wait_until(lambda: stbt.match("images/env/channel_unavailable.png")) and not stbt.wait_until(lambda: stbt.match("images/env/title_blocked.png")):
            assert stbt.wait_until(lambda: stbt.wait_for_motion()), \
"New channel " + str(ch) + " not reached on channel change number " + t 

def test_tuning_channels_20plus_times():
    for _ in " "*3: stbt.press('KEY_EXIT')
    if not stbt.wait_until(lambda: stbt.match("images/env/do_you_want_to_upgrade.png")) and not stbt.wait_until(lambda: stbt.match("images/env/channel_unavailable.png")):
        assert stbt.wait_until(lambda: stbt.wait_for_motion()), \
    "Live TV not reached at test start"
    channels = [21,24,27,29]
    t = 0
    for _ in range(5):
        for ch in channels:
            t += 1
            for x in list(str(ch)): 
                stbt.press("KEY_" + x)
                sleep(0.6)
            sleep(4)
            if stbt.match('images/dvr/continue_to_miniguide.png') and t == 1: 
                for _ in " "*2: stbt.press('KEY_RIGHT')
                for _ in " "*2: stbt.press('KEY_ENTER')
                stbt.press('KEY_RIGHT')
                stbt.press('KEY_ENTER')
            print (t)
            if not stbt.wait_until(lambda: stbt.match("images/env/do_you_want_to_upgrade.png")) and not stbt.wait_until(lambda: stbt.match("images/env/channel_unavailable.png")):
                assert stbt.wait_until(lambda: stbt.wait_for_motion()), \
    "New channel " + str(ch) + " not reached on channel change number " + t              
        
def test_play_VOD_50plus_times():
    for _ in " "*3: stbt.press('KEY_EXIT')
    VideoStore.open()

    # Find an asset that hasn't been rented yet.
    for _ in range(20):  # Try 20 assets

        # Wait for asset title to stabilise -- it loads slightly after the
        # Video Store logo appears.
        title = wait_until(lambda: VideoStore().selection, stable_secs=1)

        print "Checking asset to see if we can rent it: %s" % title
        stbt.press("KEY_ENTER")
        asset = wait_until(Asset, timeout_secs=20)

        if asset.rentable:
            print "Asset is rentable; trying to rent it"
            asset.rent()
            try:
                stbt.wait_for_motion(timeout_secs=30,
                                     mask="images/vod/mask-out-playbar.png")
                print "Successfully rented: %s" % title
                break
            except stbt.MotionTimeout:
                if UnableToPlayDialog():
                    UnableToPlayDialog().dismiss()
                else:
                    assert False, "Didn't detect video playback *nor* " \
                        "the 'Unable to Play' dialog."
                        
        stbt.press("KEY_LAST")
        assert wait_until(VideoStore), \
            "Didn't detect VideoStore main carousel after pressing back"
        stbt.press("KEY_RIGHT")
        assert wait_until(
            # pylint:disable=cell-var-from-loop
            lambda: VideoStore().selection != title), \
            "Carousel selection didn't change after pressing right"
    else:
        assert False, "Didn't find rentable playable asset after 20 attempts"

    for _ in range(50):
        stbt.press('KEY_EXIT')
        MyLibrary.open().navigate_to("Expiring Soon", title)
        #MyLibrary.open().navigate_to("Expiring Soon")        
        stbt.press('KEY_ENTER')
        assert wait_until(lambda: Asset().title == title)
        assert Asset().selected_button.text == "RESTART"
        stbt.press('KEY_ENTER')
        assert stbt.wait_for_motion(timeout_sec=20)
        
def test_DVR_playback_10plus_times_yes_TTS():
    # Turn on TTS
    for _ in " "*3: stbt.press('KEY_EXIT')
    GNarration_setting("On")
    for _ in range(10):
        count = 0
        for _ in " "*3: stbt.press('KEY_EXIT')
        sleep(2)
        if stbt.match('images/env/exit_overlay.png'):
            stbt.press('KEY_ENTER')
            sleep(2)
        sleep(3)
        stbt.press('KEY_MYDVR')
        sleep(3)
        if stbt.match('images/dvr/cancel_a_recording.png'):
            for _ in " "*2: stbt.press('KEY_RIGHT')
            for _ in " "*2: stbt.press('KEY_ENTER')
            stbt.press('KEY_RIGHT')
            stbt.press('KEY_ENTER')
        assert stbt.wait_until(lambda: stbt.match("images/dvr/my_dvr.png")), \
        "MyDVR not launched"
        while True:
            stbt.press('KEY_ENTER')
            sleep(1)
            if stbt.match('images/cta/watch.png') or stbt.match('images/cta/resume.png'): break
            count += 1
            assert count < 16, \
            "Could not find recording to play in DVR page"
        sleep(2)
        stbt.press('KEY_ENTER')
        sleep(3)
        assert stbt.wait_for_motion(timeout_secs=20)
    
def test_DVR_playback_50plus_times_no_TTS(): 
    # Turn off TTS
    for _ in " "*3: stbt.press('KEY_EXIT')
    count = 0
    #GNarration_setting("Off")
    for _ in range(51):
        count = 0
        for _ in " "*3: stbt.press('KEY_EXIT')
        sleep(3)
        stbt.press('KEY_MYDVR')
        sleep(3)
        if stbt.match('images/dvr/cancel_a_recording.png'):
            for _ in " "*2: stbt.press('KEY_RIGHT')
            for _ in " "*2: stbt.press('KEY_ENTER')
            stbt.press('KEY_RIGHT')
            stbt.press('KEY_ENTER')
        assert stbt.wait_until(lambda: stbt.match("images/dvr/my_dvr.png")), \
        "MyDVR not launched"
        while True:
            stbt.press('KEY_ENTER')
            sleep(1)
            if stbt.match('images/cta/watch.png') or stbt.match('images/cta/resume.png'): break
            count += 1
            assert count < 20, \
            "Could not find recording to play in DVR page"
        sleep(2)
        stbt.press('KEY_ENTER')
        sleep(3)
        assert stbt.wait_for_motion(timeout_secs=20)
        
def guide_launch():
    stbt.press('KEY_GUIDE')
    assert stbt.wait_until(lambda: stbt.match("images/guide/guide_options.png")), \
    "Guide not launched"
    
def menu_launch():
    for _ in " "*2: stbt.press('KEY_EXIT')
    stbt.press('KEY_MENU')
    assert stbt.wait_until(lambda: stbt.match("images/menu/menu_logo.png")), \
    "Menu not launched"

def test_random_presses_multiple_session():
    for _ in " "*3: stbt.press('KEY_EXIT')
    for _ in " "*10:
        guide_launch()
        for _ in " "*3: stbt.press('KEY_DOWN')
        for _ in " "*3: stbt.press('KEY_RIGHT')
        for _ in " "*3: stbt.press('KEY_LEFT')
        menu_launch()
        stbt.press('KEY_UP')
        stbt.press('KEY_ENTER')
        sleep(1)
        stbt.press('KEY_INFO')
        sleep(2)
        stbt.press('KEY_LAST')
        for _ in " "*2: stbt.press('KEY_OPTIONS')
        sleep(1)
        for _ in " "*3: stbt.press('KEY_EXIT')
        count = 0
        while True:
            if not stbt.wait_until(lambda: stbt.wait_for_motion(timeout_secs=10)):
                stbt.press('KEY_CHANNELUP')
            else: break
            count += 1
            assert count < 4, \
            "No motion found on Live after 4 channel changes"
        menu_launch()
        for _ in " "*5: stbt.press('KEY_UP')
        for _ in " "*2: stbt.press('KEY_DOWN')
        stbt.press('KEY_ENTER')
        for _ in " "*5: stbt.press('KEY_DOWN')
        for _ in " "*5: stbt.press('KEY_UP')
        stbt.press('KEY_LEFT')
        stbt.press('KEY_RIGHT')
        stbt.press('KEY_LEFT')
        stbt.press('KEY_RIGHT')
        stbt.press('KEY_LEFT')
        stbt.press('KEY_RIGHT')
        stbt.press('KEY_ENTER')
        for _ in " "*3: stbt.press('KEY_EXIT')
        assert stbt.wait_for_motion(timeout_secs=20)

def test_20_trickplay_buttons_on_TSB():
    for _ in " "*3: stbt.press('KEY_EXIT')
    if stbt.wait_until(lambda: stbt.match("images/dvr/pause.png")):
        stbt.press('KEY_PLAYPAUSE')
    count = 0
    while True:
        if not stbt.wait_until(lambda: stbt.wait_for_motion(timeout_secs=10)):
            stbt.press('KEY_CHANNELUP')
        else: break
        count += 1
        assert count < 4, \
        "No motion found on Live after 4 channel changes"
    sleep(2)
    stbt.press('KEY_PLAYPAUSE')
    assert stbt.wait_until(lambda: stbt.match("images/dvr/pause.png")), \
        "Unable to pause Live"
    sleep(50)
    for _ in range(5):
        stbt.press('KEY_PLAYPAUSE')
        assert stbt.wait_until(lambda: stbt.match("images/dvr/play.png")), \
            "Unable to play Live after pause"    
        stbt.press('KEY_LEFT')
        assert stbt.wait_until(lambda: stbt.match("images/dvr/rewind.png")), \
            "Unable to rewind Live"
        for _ in " "*2: stbt.press('KEY_RIGHT')
        assert stbt.wait_until(lambda: stbt.match("images/dvr/fastforward.png")), \
            "Unable to fastforward Live"
        stbt.press('KEY_PLAYPAUSE')
        assert stbt.wait_until(lambda: stbt.match("images/dvr/play.png")), \
            "Unable to play Live"
        stbt.press('KEY_PLAYPAUSE')
        assert stbt.wait_until(lambda: stbt.match("images/dvr/pause.png")), \
            "Unable to pause Live"
