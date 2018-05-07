import stbt
from stbt import wait_until

from menu import MainMenu
from transition import press_and_wait


class MyLibrary(stbt.FrameObject):
    """The top-level carousel of the Video Store.

    For more information about stb-tester FrameObjects and how to test them see
    https://stb-tester.com/tutorials/using-frame-objects-to-extract-information-from-the-screen
    """

    @property
    def is_visible(self):
        return (
            stbt.match("images/vod/my_library_logo.png", frame=self._frame) and
            not stbt.match("images/menu/menu_logo.png", frame=self._frame) and
            self.lane)

    @property
    def lane(self):
        """The title of the current selected lane ("Recently Watched", etc)."""
        return stbt.ocr(frame=self._frame,
                        region=stbt.Region(x=95, y=180, right=500, bottom=210),
                        mode=stbt.OcrMode.SINGLE_LINE)

    @property
    def selection(self):
        return stbt.ocr(
            frame=self._frame,
            region=stbt.Region(x=100, y=485, right=1220, bottom=515),
            mode=stbt.OcrMode.SINGLE_LINE)

    @staticmethod
    def open():
        menu = MainMenu.open()
        menu.navigate_to("My Library")
        stbt.press("KEY_ENTER")
        my_library = wait_until(MyLibrary)
        assert my_library, "Didn't detect My Library main carousel"
        return my_library

    def navigate_to(self, lane, title):
        # Find the target lane. This assumes we're starting from the top lane.
        for _ in range(5):
            if MyLibrary().lane == lane:
                print "Found lane %s" % lane
                break
            press_and_wait("KEY_DOWN")
        else:
            assert False, \
                "Didn't find lane %r after pressing down 5 times" % lane

        for _ in range(20):
            if MyLibrary().selection == title:
                print "Found title %r" % title
                break
            press_and_wait("KEY_RIGHT")
        else:
            assert False, \
                "Didn't find title %r after pressing right 20 times" % title

    def find_lane(self, lane):
        # Find the target lane. This assumes we're starting from the top lane.
        for _ in range(6):
            if MyLibrary().lane == lane:
                print "Found lane %s" % lane
                break
            press_and_wait("KEY_DOWN")
        else:
            assert False, \
                "Didn't find lane %r after pressing down 5 times" % lane
