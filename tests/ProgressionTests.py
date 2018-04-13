import stbt
import api_test
from stbt import wait_until
from my_library import MyLibrary
from video_store import Asset, VideoStore
from dialogs import UnableToPlayDialog

def mydvr_launch():
    stbt.press('KEY_EXIT')
    stbt.press('KEY_MYDVR')
    assert stbt.wait_until(lambda: stbt.match("images/dvr/my_dvr.png")), \
    "MyDVR not launched"

def test_tuning_channels_200plus_times():
    stbt.press('KEY_EXIT')
    stbt.press('KEY_EXIT')
    stbt.press('KEY_EXIT')
    for _ in range(50):
        channels = [1,2,3,4,5,6,7,8,9]
        for ch in channels:
            for x in list(ch): stbt.press('KEY_'+'str(x)')
            assert stbt.wait_for_motion()               
        
def test_play_VOD_50plus_times():
    VideoStore.open()

    # Find an asset that hasn't been rented yet.
    for _ in range(20):  # Try 20 assets

        # Wait for asset title to stabilise -- it loads slightly after the
        # Video Store logo appears.
        title = wait_until(lambda: VideoStore().selection, stable_secs=1)

        print "Checking asset to see if we can rent it: %s" % title
        stbt.press("KEY_ENTER")
        asset = wait_until(Asset, timeout_secs=20)
        assert asset, "Didn't detect asset page"
        assert asset.title == title, \
            "Loaded asset page for %r but expected %r" % (asset.title, title)

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
        
def test_DVR_playback_50plus_times_yes_TTS():
    # Turn on TTS
    
    for _ in range(51):
        mydvr_launch()
        while True:
            stbt.press('KEY_ENTER')
        sleep(1)
            if stbt.match('images/cta/watch.png'): break
            count += 1
            assert count < 16, \
            "Could not find recording to play in DVR page"
        stbt.press('KEY_ENTER')
        assert stbt.wait_for_motion(timeout_secs=20)
    
def test_DVR_playback_50plus_times_no_TTS(): 
    # Turn off TTS
    
    for _ in range(51):
        mydvr_launch()
        while True:
            stbt.press('KEY_ENTER')
        sleep(1)
            if stbt.match('images/cta/watch.png'): break
            count += 1
            assert count < 16, \
            "Could not find recording to play in DVR page"
        stbt.press('KEY_ENTER')
        assert stbt.wait_for_motion(timeout_secs=20)
