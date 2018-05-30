import time
from tests.SpectrumGuide.ObjectRepo import LiveTV


def exit_to_live_tv_screen(step_name, user, number_of_exit_key=1, wait_after_key_press_secs=1):
    """
    :author: SivaRam Kumar Mani
    :description: exit to live tv screen from any screen using exit key press
    :param step_name:
    :param user:
    :param number_of_exit_key:
    :param wait_after_key_press_secs:
    :return:
    """
    user.remote_control_press('KEY_EXIT', number_of_exit_key)
    if user.check_motion(motion_time_out_secs=10):
        user.LogResults.passed("{}: Exit from current screen to Live TV Screen using {} EXIT key".format
                               (step_name, number_of_exit_key))
        time.sleep(wait_after_key_press_secs)
        return True
    else:
        user.LogResults.failed("{} To Exit from current screen to Live TV Screen".format(step_name, number_of_exit_key))
        return False


def turn_box_on(step_name, user, wait_after_power_press_secs=10):
    """
    :author: Beau Yoder
    :description: presses Power if black screen is found
    :param step_name:
    :param user:
    :param wait_after_power_press_secs:
    :return:
    """
    if user.check_motion(motion_time_out_secs=10):
        user.LogResults.passed("{}: Box detected as powered ON".format(step_name))
        return True
    if user.check_image(LiveTV.black_screen["image"]):
        user.remote_control_press('KEY_POWER')
        time.sleep(wait_after_power_press_secs)
    if user.check_image(LiveTV.black_screen["image"]):
        user.LogResults.failed("{}: Box unable to turn ON".format(step_name))
        return False
