def init():
    if stbt.match('images/env/user_settings.png'):
        for _ in " "*2: stbt.press('KEY_POWER')
    else:
        stbt.press('KEY_EXIT')
        stbt.press('KEY_EXIT')
        guide_launch()
        stbt.press('KEY_EXIT')
