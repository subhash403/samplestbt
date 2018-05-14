import stbt
from stbt import wait_until

from dialogs import ConfirmRentalDialog, SelectedButton
from menu import MainMenu


class VideoStore(stbt.FrameObject):
    """The top-level carousel of the Video Store.

    For more information about stb-tester FrameObjects and how to test them see
    https://stb-tester.com/tutorials/using-frame-objects-to-extract-information-from-the-screen
    """

    @property
    def is_visible(self):
        return stbt.match("images/vod/video_store_logo.png", frame=self._frame)

    @property
    def selection(self):
        return stbt.ocr(
            frame=self._frame,
            region=stbt.Region(x=100, y=500, right=1220, bottom=530),
            mode=stbt.OcrMode.SINGLE_LINE)

    @staticmethod
    def open():
        menu = MainMenu.open()
        menu.navigate_to("Video Store")
        stbt.press("KEY_ENTER")
        video_store = wait_until(VideoStore)
        assert video_store, "Didn't detect VideoStore main carousel"
        return video_store


class Asset(stbt.FrameObject):
    """The asset page for an asset in the video store."""

    @property
    def is_visible(self):
        # Most of the content on an Asset page is different for each asset.
        # The only things that are consistently the same:
        # * There are buttons (like "RENT $2.99", "ADD TO WATCHLIST", etc)
        #   and the first button is selected (solid).
        # * Heading "Cast & Crew" in the bottom half of the screen.
        return (self.selected_button and
                stbt.match_text("Cast & Crew", frame=self._frame))

    @property
    def title(self):
        return stbt.ocr(
            frame=self._frame,
            region=stbt.Region(x=320, y=120, right=1220, bottom=190))

    @property
    def rentable(self):
        return "RENT" in self.selected_button.text

    @property
    def selected_button(self):
        return SelectedButton(self._frame)

    def rent(self):
        assert self.rentable, "Asset isn't rentable"
        stbt.press("KEY_ENTER")
        assert wait_until(ConfirmRentalDialog), \
            "Didn't find 'Confirm Rental' dialog"
        ConfirmRentalDialog().confirm()
