import stbt
from stbt import wait_until


def detect_dialog():
    """Returns a `ModalDialog` sub-class, or None if no dialog is detected."""
    for klass in [StillThereDialog, ExitDialog, ConfirmRentalDialog,
                  UnableToPlayDialog]:
        d = klass()
        if d.is_visible:
            return d
    return None


class ModalDialog(stbt.FrameObject):

    TITLE_REGION = stbt.Region(x=300, y=170, right=900, bottom=280)

    @property
    def is_visible(self):
        """Must be over-ridden by sub-classes."""
        return False

    def dismiss(self):
        """Sub-classes must implement this method."""
        raise NotImplementedError()


class StillThereDialog(ModalDialog):
    """The "Still There?" dialog with a 30-second countdown timer."""

    @property
    def is_visible(self):
        return stbt.match_text("Still There?", frame=self._frame,
                               region=self.TITLE_REGION)

    def dismiss(self):
        # There's a slight race condition here: If we detect the dialog when
        # there's like 1 second left in the countdown, by the time the script
        # calls `dismiss()` the dialog might have disappeared already. In that
        # case pressing EXIT will dump us back to live TV. This may not be a
        # problem in practice.
        stbt.press("KEY_EXIT")
        assert wait_until(lambda: not StillThereDialog()), \
            "'Still There?' dialog didn't disappear after pressing EXIT"


class ExitDialog(ModalDialog):
    """The "Exit?" dialog when you try to stop watching a vod asset."""

    @property
    def is_visible(self):
        return stbt.match_text(
            "Exit?", frame=self._frame,
            region=stbt.Region(x=270, y=240, right=1000, bottom=320))

    def exit(self):
        stbt.press("KEY_ENTER")
        assert wait_until(lambda: not ExitDialog()), \
            "'Exit?' dialog didn't disappear after selecting EXIT"

    def dismiss(self):
        self.exit()


class ConfirmRentalDialog(ModalDialog):
    """The "Confirm Rental" modal dialog (with "confirm" & "cancel" buttons)."""

    @property
    def is_visible(self):
        return stbt.match_text("Confirm Rental", frame=self._frame,
                               region=self.TITLE_REGION)

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
        assert wait_until(lambda: not ConfirmRentalDialog()), \
            "'Confirm Rental' dialog didn't disappear after selecting CANCEL"

    def confirm(self):
        if self.selection == "CONFIRM":
            stbt.press("KEY_ENTER")
        else:
            stbt.press("KEY_LEFT")
            assert wait_until(
                lambda: ConfirmRentalDialog().selection == "CONFIRM"), \
                "Failed to select dialog's CONFIRM button"
            stbt.press("KEY_ENTER")
        assert wait_until(lambda: not ConfirmRentalDialog()), \
            "'Confirm Rental' dialog didn't disappear after selecting CONFIRM"

    def dismiss(self):
        self.cancel()


class UnableToPlayDialog(ModalDialog):
    """The "Unable to Play" modal dialog (with error code and "OK" button)."""

    @property
    def is_visible(self):
        return stbt.match_text("Unable to Play", frame=self._frame,
                               region=self.TITLE_REGION)

    def dismiss(self):
        stbt.press("KEY_ENTER")
        assert wait_until(lambda: not UnableToPlayDialog()), \
            "'Unable to Play' dialog didn't disappear after selecting OK"


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
