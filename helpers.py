
import pyautogui as gui
import math
import time
import os

def start_tarkov():
    gui.click('.\img\win_icon.PNG', duration=1)
    gui.write("battlestate games")
    time.sleep(0.25)
    gui.press('enter')
    wait_until_img_appears('.\img\play.PNG')
    gui.click('.\img\play.PNG')

    pass

def wait_until_img_appears(image_paths, max_tries=3, confidence=0.9, exit_on_fail=True, sleep_time_sec=1):
    try_count = 0
    location = None

    while not location and try_count < max_tries:
        for img_path in image_paths:
            location = gui.locateCenterOnScreen(os.path.join("./img", img_path), confidence=confidence)
            if location:
                break
            time.sleep(sleep_time_sec)
            try_count += 1

    if exit_on_fail and not location:
        exit("Failed to find any of the following images: {}".format(image_paths))

    return location

