#!/usr/bin/env python
# coding=utf-8
"""
This file contains regression tests automatically generated by
``stbt auto-selftest``. These tests are intended to capture the
behaviour of Frame Objects (and other helper functions that operate on
a video-frame). Commit this file to git, re-run ``stbt auto-selftest``
whenever you make a change to your Frame Objects, and use ``git diff``
to see how your changes affect the behaviour of the Frame Object.

NOTE: THE OUTPUT OF THE DOCTESTS BELOW IS NOT NECESSARILY "CORRECT" --
it merely documents the behaviour at the time that
``stbt auto-selftest`` was run.
"""
# pylint: disable=line-too-long

import os
import sys

sys.path.insert(0, os.path.join(
    os.path.dirname(__file__), '../../../tests'))

from menu import *  # isort:skip pylint: disable=wildcard-import, import-error

_FRAME_CACHE = {}


def f(name):
    img = _FRAME_CACHE.get(name)
    if img is None:
        import cv2
        filename = os.path.join(os.path.dirname(__file__),
                                '../../screenshots', name)
        img = cv2.imread(filename)
        assert img is not None, "Failed to load %s" % filename
        img.flags.writeable = False
        _FRAME_CACHE[name] = img
    return img


def auto_selftest_MainMenu():
    r"""
    >>> MainMenu(frame=f("New box/Menu/Guide.png"))
    MainMenu(is_visible=True, selection=u'Guide')
    >>> MainMenu(frame=f("New box/Menu/My Library.png"))
    MainMenu(is_visible=True, selection=u'My Library')
    >>> MainMenu(frame=f("Worldbox/Menu/My Library.png"))
    MainMenu(is_visible=True, selection=u'My Library')
    >>> MainMenu(frame=f("Worldbox/Menu/Video Store.png"))
    MainMenu(is_visible=True, selection=u'Video Store')
    """
    pass
