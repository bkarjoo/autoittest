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


def mouse_double_click():
    pyautogui.click()
    time.sleep(.1)
    pyautogui.click()
