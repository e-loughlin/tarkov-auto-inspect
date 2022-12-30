from helpers import *
import pyautogui as gui
import time

# Start this script while you have the game open, and you're in the main menu.

if __name__ == "__main__":
    print("Ensure you have the main menu of Tarkov open...")
    time.sleep(3)

    x = wait_until_img_appears(["main_menu.png", "main_menu2.png"], 10)
    gui.click(x)

    x = wait_until_img_appears(["trader1.png", "trader2.png"], 10)
    gui.click(x)

    traders = ["prapor.png", "therapist.png", "fence.png", "skier.png", "peacekeeper.png", "mechanic.png", "ragman.png"]

    for t in traders: 
        print(t.split(".")[0])
        x = wait_until_img_appears([t], 10)
        gui.click(x)

        all_item_sets_button = wait_until_img_appears(["all_item_sets.png"])
        gui.click(all_item_sets_button)

        while(True):
            x = wait_until_img_appears(["gray1.png", "gray2.png", "gray3.png", "gray4.png", "gray5.png", "gray6.png", "gray7.png", "gray8.png", "gray9.png", "gray10.png"], confidence=0.98, exit_on_fail=False, sleep_time_sec=0)
            if x:
                gui.click(x, button="middle")
                continue
            else:
                scrolling_done = wait_until_img_appears(["finish_scroll.png"], max_tries=1, exit_on_fail=False, confidence=0.99, sleep_time_sec=0)
                # If scrolling down to bottom is complete, end search
                if scrolling_done:
                    print("Done!")
                    break
                # Otherwise keep scrolling down
                else:
                    print("scrolling...")
                    gui.moveTo(all_item_sets_button)
                    gui.moveRel(0, 150)

                    for _ in range(10):
                        gui.scroll(-5)

        x = wait_until_img_appears(["trader1.png", "trader2.png"], 10)
        gui.click(x)


