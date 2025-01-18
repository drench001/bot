
import os
import cv2
import math
import time
import pyautogui
import statistics

from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats




def calc_distance(
        start_coords: tuple, 
        end_coords: tuple
        ) -> float:
    """Compute total distance between two coords"""

    # find distance traveled
    x = (end_coords[0]-start_coords[0])
    y = (end_coords[1]-start_coords[1])
    dist = math.sqrt(x**2 + y**2)

    return dist



# normal distribution
def get_normal_dist_values(
        center: int, 
        spread: int, 
        count: int, 
        plot = False
) -> list[float]:
    
    values = np.random.normal(
        center, 
        spread, 
        count
        )
    
    if plot:
        fig = plt.hist(values, bins=100)
        plt.title('Standard Distribution')
        plt.xlabel("Returned Value")
        plt.ylabel("Frequency")
        plt.text(
            max(fig[1]),
            max(fig[0]),
            horizontalalignment='right',
            verticalalignment='top',
            s=f'Median: {round(statistics.median(values), 3)}\nMax: {round(max(values), 3)}\nMin: {round(min(values), 3)}\nRange: {round(max(values)-min(values), 3)}',
            )
        plt.axvline(statistics.median(values), color='red', linestyle='--')
        plt.show()

    return values


def get_beta_dist_values(
        alpha: int, 
        beta: int, 
        center: int, 
        count: int,
        plot = False
) -> list[float]:
    
    """Get values from a beta distribution with option to plot"""
    
    values = stats.beta.rvs(
            alpha,
            beta,
            loc=center,
            size=count
        )
    
    if plot:
        fig = plt.hist(values, bins=100)
        plt.title('Beta Distribution')
        plt.xlabel("Returned Value")
        plt.ylabel("Frequency")
        plt.text(
            max(fig[1]),
            max(fig[0]),
            horizontalalignment='right',
            verticalalignment='top',
            s=f'Median: {round(statistics.median(values), 3)}\nMax: {round(max(values), 3)}\nMin: {round(min(values), 3)}\nRange: {round(max(values)-min(values), 3)}',
            )
        plt.axvline(statistics.median(values), color='red', linestyle='--')
        plt.show()

    return values



# get_normal_dist_values(
#     center=20, 
#     spread=1, 
#     count=10000, 
#     plot=True
#     )

# get_beta_dist_values(
#     alpha=4,
#     beta=24,
#     center=0,
#     count=10000,
#     plot=True
# )




# uncomment this to get a mouse position in terminal
# pyautogui.displayMousePosition()
show_mouse = False
if show_mouse:
    pyautogui.displayMousePosition()


# to not get caught need to randomize: 
#   - scroll speed (single duration value)
#   - click duration (single duration value)
#   - location (x and y)


# move the mouse to coordinates
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
    coords = pyautogui.center(
            pyautogui.locateOnScreen(
            filepath,
            confidence,
        )
    )
    print(f'Coords: {coords}')



run = False
if run:
    # save a file of a selected portion of the screen
    def calibrate(save_filename: Path | None = False):
        print('Switch to desired screen, 2s pause...')
        time.sleep(2)
        clipboard_data = pyautogui.screenshot()
        clipboard_data.save("image.png", "PNG")
        image = cv2.imread("image.png")
        selection = cv2.selectROI("image", image)
        x, y, w, h = selection
        cropped = image[y:y+h, x:x+w]
        #cv2.imshow('image', cropped)
        cv2.destroyAllWindows()
        os.remove("image.png")
        if save_filename:
            print(cv2.imwrite(save_filename, cropped))
            print(f'saving to {save_filename}')
        return selection
    
    print(Path('/Users/drench/python/screen_test.png').is_file())
    calibrate('/Users/drench/python/screen_test.png')


