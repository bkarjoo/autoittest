import pyautogui
import time


def mouse_position():
    return pyautogui.position()


def move_mouse(p):
    if p == None: return
    try:
        pyautogui.moveTo(p[0],p[1])
    except Exception as e:
        pass


def mouse_click():
    pyautogui.click()


def mouse_right_click():
    pyautogui.click(button='right')


def mouse_double_click():
    pyautogui.click()
    time.sleep(.1)
    pyautogui.click()


def mouse_click_at(point):
    # move mouse to the point first then click
    move_mouse(point)
    pyautogui.click()


def mouse_double_click_at(point):
    # two single clicks with delay in between is more accurate
    # than requesting pyautogui clicks=2
    move_mouse(point)
    pyautogui.click(clicks=1)
    time.sleep(.1)
    pyautogui.click(clicks=1)


def mouse_drag(point):
    pyautogui.dragTo(point[0], point[1], duration=1)
