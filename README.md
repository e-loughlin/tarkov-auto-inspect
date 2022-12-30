# tarkov-auto-inspect

You can run this Python script while you have Escape from Tarkov open. It will go into your traders and automatically locate all items you have not identified, and it will identify them.

## Requirements

- Python 3

## Instructions

1. Clone this repository.
2. Open Escape from Tarkov. Make sure you're at the main screen.
3. In a `cmd` prompt (Windows Command Prompt, or Powershell, for example) navigate to where you cloned the repository.
4.  Run `python -m pip install -r requirements.txt`. 
5. Run `python inspect_items.py`.
6. Click on the menu somewhere in the game and the script should start running. Hands off the mouse and keyboard. It will go through each of the traders and inspect all the items; scrolling to the bottom while searching for each one.

## YouTube Demo

https://www.youtube.com/watch?v=SflZCmJArgU&feature=youtu.be

## If It's Not Working

1. If the script is failing, it may be because your resolution / video settings differ from mine when I took the screenshots. This script uses `pyautogui` and relies on matching screenshots. Therefore, if your screen doesn't match the screenshots provided, it might not work. You could resolve this problem by taking your own screenshots and replacing the images in the `img` directory. For each of the `gray.png` images, these are the alpha backgrounds of unsearched items that the script is looking for. There are many of them because there are many different colour schemes for various different unidentified items. 

2. Currently, Jaeger isn't supported. This is simply because at the time I wrote this script, I didn't have Jaeger unlocked and couldn't screenshot his image. You can fix this by:

  - Screenshotting Jaeger's face and saving "jaeger.png" in the `img` directory.
  - Adding `"jaeger.png"` to the line in `inspect_items.py` that specifies the list of traders, i.e. change it to `traders = ["prapor.png", "therapist.png", "fence.png", "skier.png", "peacekeeper.png", "mechanic.png", "ragman.png", "jaeger.png"]`
