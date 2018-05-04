import stbt
from stbt import wait_until

from dialogs import detect_dialog, ModalDialog
from transition import press_and_wait


class MainMenu(stbt.FrameObject):
    """The main "Spectrum" menu (Search / Guide / My Library / etc).

    For more information about stb-tester FrameObjects and how to test them see
    https://stb-tester.com/tutorials/using-frame-objects-to-extract-information-from-the-screen
    """

    MENU_ITEMS = ["Search", "Guide", "My Library", "TV Shows", "Movies",
                  "Video Store", "Settings & Support"]
    MENU_ITEMS_REGION = stbt.Region(x=0, y=180, right=300, bottom=720)

    @property
    def is_visible(self):
        return (
            stbt.match("images/menu/menu_logo.png",
                       frame=self._frame,
                       region=stbt.Region(x=0, y=0, right=300, bottom=180)) and
            self.selection in self.MENU_ITEMS)

    @property
    def selection(self):
        return _ocr(
            frame=self._frame,
            region=self.MENU_ITEMS_REGION,
            text_color=(220, 219, 214), text_color_threshold=50,
            tesseract_user_words=self.MENU_ITEMS)

    @staticmethod
    def open():
        # If the menu's already open, don't need to press anything.
        menu = MainMenu()
        if menu:
            return menu

        stbt.press("KEY_MENU")
        menu_or_dialog = wait_until(lambda: MainMenu() or detect_dialog())
        if isinstance(menu_or_dialog, ModalDialog):
            menu_or_dialog.dismiss()
            menu = wait_until(MainMenu)
            if not menu:
                stbt.press("KEY_MENU")
                menu = wait_until(MainMenu)
        else:
            menu = menu_or_dialog
        assert menu, "Failed to find main menu after pressing KEY_MENU"
        return menu

    def navigate_to(self, target):
        assert target in self.MENU_ITEMS, \
            "Invalid target %r; expected one of %r" % (target, self.MENU_ITEMS)

        for key in self._navigate_keys(self.selection, target):
            press_and_wait(key, region=self.MENU_ITEMS_REGION)
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


def _ocr(frame, text_color, text_color_threshold,
         region=stbt.Region.ALL,
         mode=stbt.OcrMode.PAGE_SEGMENTATION_WITHOUT_OSD,
         lang=None, tesseract_config=None, tesseract_user_words=None,
         tesseract_user_patterns=None):

    """This implements custom thresholding because stbt.ocr doesn't allow you to
    specify a custom text_color threshold.

    This can be removed when Stb-tester v29 is released.

    Accepts the same parameters as stbt.ocr:
    <https://stb-tester.com/manual/python-api#stbt.ocr>
    """

    import cv2
    import numpy

    frame = stbt.crop(frame, region)

    # We scale image up 3x before feeding it to tesseract as this
    # significantly reduces the error rate by more than 6x in test_repo.  This
    # uses bilinear interpolation which produces the best results.  See
    # http://stb-tester.com/blog/2014/04/14/improving-ocr-accuracy.html
    #
    # This must be done before thresholding.
    outsize = (frame.shape[1] * 3, frame.shape[0] * 3)
    frame = cv2.resize(frame, outsize, interpolation=cv2.INTER_LINEAR)

    # Calculate distance of each pixel from `text_color`, then discard
    # everything further than `text_color_threshold` distance away.
    diff = numpy.subtract(frame, text_color, dtype=numpy.int32)
    frame = numpy.sqrt((diff[:, :, 0] ** 2 +
                        diff[:, :, 1] ** 2 +
                        diff[:, :, 2] ** 2) / 3) \
                 .astype(numpy.uint8)
    _, frame = cv2.threshold(frame, text_color_threshold, 255,
                             cv2.THRESH_BINARY)

    return stbt.ocr(frame, mode=mode, lang=lang,
                    tesseract_config=tesseract_config,
                    tesseract_user_words=tesseract_user_words,
                    tesseract_user_patterns=tesseract_user_patterns,
                    upsample=False)
