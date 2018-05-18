
from tests.SpectrumGuide.ObjectRepo import GuideScreen


def select_future_program_using_right_arrow(step_name, user, number_of_times_to_move_right=1):
    # Verify 'RIGHT KEY highlight future program'
    user.remote_control_press('KEY_RIGHT',number_of_times_to_move_right)
    if user.check_image(GuideScreen.first_cell_not_selected["image"], GuideScreen.first_cell_not_selected["region"]) :
        user.LogResults.passed("{}: Right press moves to next future program in guide".format(step_name))
        return True
    else:
        user.LogResults.failed("{}: Right press did not move to next future program in guide".format(step_name))
        return False


def move_in_guide_using_down_arrow(step_name, user, number_of_times_to_move_down=1):
    # Verify 'RIGHT KEY highlight future program'
    user.remote_control_press('KEY_DOWN',number_of_times_to_move_down)
    user.LogResults.info("{}: Down Key press move program in guide".format(step_name))
    return True


def check_page_down_channel_scrolling(step_name,user):
    # Verify 'PAGE_DOWN' press shifts down the list by 5,
    last_channel = user.get_text(GuideScreen.last_channel["region"])
    user.LogResults.info("Identified Channel " + last_channel + " at bottom of guide table")
    user.remote_control_press('KEY_PAGEDOWN')
    first_channel = user.get_text(GuideScreen.first_channel["region"])
    if last_channel == first_channel:
        user.LogResults.passed("{}: Page_Down press moves down the guide by 5 channels".format(step_name))
        return True
    else:
        user.LogResults.failed("{}: Page_Down press did not move the guide by 5 channels".format(step_name))
        return False


def check_page_up_channel_scrolling(step_name,user):
    # Verify 'PAGE_UP' press shifts up the list by 5,
    first_channel = user.get_text(GuideScreen.first_channel["region"])
    user.remote_control_press('KEY_PAGEUP')
    last_channel = user.get_text(GuideScreen.last_channel["region"])
    user.LogResults.info("Identified Channel " + last_channel + " at bottom of guide table")
    if last_channel == first_channel:
        user.LogResults.passed("{}: Page_Up press moves up the guide by 5 channels".format(step_name))
        return True
    else:
        user.LogResults.failed("{}: Page_Up press did not move the guide by 5 channels".format(step_name))
        return False
