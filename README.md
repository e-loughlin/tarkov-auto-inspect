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

## Caveats

If the script is failing, you may need to adjust your resolution / video settings. Sorry. This script uses `pyautogui` and relies on matching screenshots. If your screen doesn't match the screenshots provided, it might not work.
