import stbt
from stbt import wait_until

from my_library import MyLibrary
from video_store import Asset, UnableToPlayDialog, VideoStore


def test_asset_rental():
    VideoStore.open()

    # Find an asset that hasn't been rented yet.
    for _ in range(20):  # Try 20 assets

        # Wait for asset title to stabilise -- it loads slightly after the
        # Video Store logo appears.
        title = wait_until(lambda: VideoStore().selection, stable_secs=1)

        print "Checking asset to see if we can rent it: %s" % title
        stbt.press("KEY_ENTER")
        asset = wait_until(Asset)
        assert asset, "Didn't detect asset page"
        assert asset.title == title, \
            "Loaded asset page for %r but expected %r" % (asset.title, title)

        if asset.rentable:
            print "Asset is rentable; trying to rent it"
            asset.rent()
            try:
                stbt.wait_for_motion(timeout_secs=30,
                                     mask="images/vod/mask-out-playbar.png")
                break
            except stbt.MotionTimeout:
                # Beau says:
                #
                # > many assets displayed in the video store will present the
                # > option to rent/watch, but an error can be thrown, as we are
                # > developing/testing in a development environment.
                #
                # So we'll ignore the "Unable to Play" dialog and try the next
                # asset until we find a rentable, playable one.
                if UnableToPlayDialog():
                    UnableToPlayDialog().dismiss()
                else:
                    assert False, "Didn't detect video playback *nor* " \
                        "the 'Unable to Play' dialog."

        # Go back and try the next asset.
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

    MyLibrary.open().navigate_to("Expiring Soon", title)
    stbt.press("KEY_ENTER")
    assert wait_until(lambda: Asset().title == title)
    assert Asset().selected_button.text == "RESTART"
