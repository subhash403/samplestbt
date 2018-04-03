import stbt
from stbt import wait_until

from my_library import MyLibrary
from video_store import VideoStore, Asset


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
            print "Asset is rentable"
            break
        else:
            stbt.press("KEY_LAST")
            assert wait_until(VideoStore), \
                "Didn't detect VideoStore main carousel after pressing back"
            stbt.press("KEY_RIGHT")
            assert wait_until(
                # pylint:disable=cell-var-from-loop
                lambda: VideoStore().selection != title), \
                "Carousel selection didn't change after pressing right"
    else:
        assert False, "Didn't find rentable asset after 20 attempts"

    # TODO: Find another asset if playback fails.
    asset.rent()
    assert stbt.wait_for_motion(timeout_secs=30,
                                mask="images/vod/mask-out-playbar.png")

    MyLibrary.open().navigate_to("Expiring Soon", title)
    stbt.press("KEY_ENTER")
    assert wait_until(lambda: Asset().title == title)
    assert Asset().selected_button.text == "RESTART"
