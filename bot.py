



'mkdir python'
'mkdir venv'
'brew install python'
# get the path from the command return

# make the virtual environment
'<path from command above>/bin/python -m venv ~/venv'

# install the libraries
'~/venv/bin/pip install pyautogui opencv-python'

# run the script
'~/venv/bin/python ~/python/bot.py'



import cv2
import pyautogui

from pathlib import Path



# uncomment this to get a mouse position in terminal
# pyautogui.displayMousePosition()




# to not get caught need to randomize: 
#   - scroll speed (single duration value)
#   - click duration (single duration value)
#   - location (x and y)


# move the mouse
run = False
if run:
    duration = 2
    position_1 = pyautogui.moveTo(
        (768, 240),
        duration=duration
        )



# find an image on the screen
run = False
if run:
    filepath = ''
    confidence = .99
    # region - can speed up later
    pyautogui.locateOnScreen(
        filepath,
        confidence,
    )



run = True
if run:
    # save a file of a selected portion of the screen
    def calibrate(save_filename: Path | None = False):
        clipboard_data = pyautogui.screenshot()
        clipboard_data.save("image.png", "PNG")
        image = cv2.imread("image.png")
        selection = cv2.selectROI("image", image)
        x, y, w, h = selection
        cropped = image[y:y+h, x:x+w]
        #cv2.imshow('image', cropped)
        cv2.destroyAllWindows()
        if save_filename:
            cv2.imwrite(save_filename, cropped)
        return selection
    
    calibrate()