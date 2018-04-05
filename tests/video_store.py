import stbt
from stbt import wait_until

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


class ConfirmRentalDialog(stbt.FrameObject):
    """The "Confirm Rental" modal dialog (with "confirm" & "cancel" buttons)."""

    @property
    def is_visible(self):
        return stbt.match_text(
            "Confirm Rental", frame=self._frame,
            region=stbt.Region(x=300, y=170, right=900, bottom=280))

    @property
    def selection(self):
        return SelectedButton(self._frame).text

    def cancel(self):
        if self.selection == "CANCEL":
            stbt.press("KEY_ENTER")
        else:
            stbt.press("KEY_RIGHT")
            assert wait_until(
                lambda: ConfirmRentalDialog().selection == "CANCEL"), \
                "Failed to select dialog's CANCEL button"
            stbt.press("KEY_ENTER")

    def confirm(self):
        if self.selection == "CONFIRM":
            stbt.press("KEY_ENTER")
        else:
            stbt.press("KEY_LEFT")
            assert wait_until(
                lambda: ConfirmRentalDialog().selection == "CONFIRM"), \
                "Failed to select dialog's CONFIRM button"
            stbt.press("KEY_ENTER")


class UnableToPlayDialog(stbt.FrameObject):
    """The "Unable to Play" modal dialog (with error code and "OK" button)."""

    @property
    def is_visible(self):
        return stbt.match_text(
            "Unable to Play", frame=self._frame,
            region=stbt.Region(x=300, y=170, right=900, bottom=280))

    def dismiss(self):
        stbt.press("KEY_EXIT")
        assert wait_until(lambda: not UnableToPlayDialog()), \
            "'Unable to Play' dialog didn't disappear after pressing EXIT"


class SelectedButton(stbt.FrameObject):
    """Finds the selected (solid) button by matching the left & right edges."""

    @property
    def is_visible(self):
        return self._left_edge and self._right_edge

    @property
    def text(self):
        r = stbt.Region(x=self._left_edge.region.right,
                        y=self._left_edge.region.y,
                        right=self._right_edge.region.x,
                        bottom=self._left_edge.region.bottom)
        return stbt.ocr(frame=self._frame, region=r,
                        mode=stbt.OcrMode.SINGLE_LINE)

    @property
    def _left_edge(self):
        return stbt.match("images/vod/selected-button-left-edge.png",
                          frame=self._frame)

    @property
    def _right_edge(self):
        return stbt.match("images/vod/selected-button-right-edge.png",
                          frame=self._frame)
