import keyboard
from time import sleep

def control_a():
    sleep(.1)
    keyboard.press('ctrl')
    sleep(.1)
    keyboard.press_and_release('a')
    sleep(.1)
    keyboard.release('ctrl')
    sleep(.1)


def control_c():
    sleep(.1)
    keyboard.press('ctrl')
    sleep(.1)
    keyboard.press_and_release('c')
    sleep(.1)
    keyboard.release('ctrl')
    sleep(.1)


def control_v():
    sleep(.1)
    keyboard.press('ctrl')
    sleep(.1)
    keyboard.press_and_release('v')
    sleep(.1)
    keyboard.release('ctrl')
    sleep(.1)


def write(some_string):
    keyboard.write(some_string)


def up_arrow():
    keyboard.send('up')
    sleep(.05)


def down_arrow():
    keyboard.send('down')
    sleep(.05)


def delete():
    keyboard.send('delete')
    sleep(.05)
