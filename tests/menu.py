import time

import stbt
from stbt import wait_until


class MainMenu(stbt.FrameObject):
    """The main "Spectrum" menu (Search / Guide / My Library / etc).

    For more information about stb-tester FrameObjects and how to test them see
    https://stb-tester.com/tutorials/using-frame-objects-to-extract-information-from-the-screen
    """

    MENU_ITEMS = ["Search", "Guide", "My Library", "TV Shows", "Movies",
                  "Video Store", "Settings & Support"]

    @property
    def is_visible(self):
        return stbt.match("images/menu/menu_logo.png",
                          frame=self._frame,
                          region=stbt.Region(x=0, y=0, right=300, bottom=180))

    @property
    def selection(self):
        selected_text = stbt.ocr(
            frame=self._frame,
            region=stbt.Region(x=0, y=180, right=300, bottom=720),
            text_color=(241, 235, 230),
            tesseract_user_words=self.MENU_ITEMS)
        assert selected_text in self.MENU_ITEMS, \
            "Read unexpected menu item %r; expected one of %r" % (
                selected_text, self.MENU_ITEMS)
        return selected_text

    @staticmethod
    def open():
        # If the menu's already open, don't need to press anything.
        menu = MainMenu()
        if menu:
            return menu

        stbt.press("KEY_MENU")
        menu = wait_until(MainMenu)
        assert menu, "Failed to find main menu after pressing KEY_MENU"
        return menu

    def navigate_to(self, target):
        assert target in self.MENU_ITEMS, \
            "Invalid target %r; expected one of %r" % (target, self.MENU_ITEMS)

        for key in self._navigate_keys(self.selection, target):
            stbt.press(key)
            time.sleep(1)
        new_frame = wait_until(lambda: MainMenu().selection == target)
        assert new_frame, "Failed to reach menu target %r" % target
        return new_frame

    @staticmethod
    def _navigate_keys(source, target):
        """
        >>> MainMenu._navigate_keys("My Library", "Video Store")
        ['KEY_DOWN', 'KEY_DOWN', 'KEY_DOWN']
        >>> MainMenu._navigate_keys("Video Store", "My Library")
        ['KEY_UP', 'KEY_UP', 'KEY_UP']
        >>> MainMenu._navigate_keys("Video Store", "Video Store")
        []
        """
        diff = (MainMenu.MENU_ITEMS.index(target) -
                MainMenu.MENU_ITEMS.index(source))
        key = "KEY_DOWN" if diff > 0 else "KEY_UP"
        return [key] * abs(diff)
