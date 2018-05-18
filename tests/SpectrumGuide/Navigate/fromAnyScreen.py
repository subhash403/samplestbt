import time


def exit_to_live_tv_screen(step_name, user, number_of_exit_key=1,wait_after_key_press_secs=1):
    user.remote_control_press('KEY_EXIT', times=number_of_exit_key)
    if user.check_motion(motion_timeout=10) :
        user.LogResults.passed("{} Exit from current screen to Live TV Screen using {} EXIT key".format(step_name, number_of_exit_key))
        time.sleep(wait_after_key_press_secs)
        return True
    else:
        user.LogResults.failed("{} To Exit from current screen to Live TV Screen".format(step_name, number_of_exit_key))

