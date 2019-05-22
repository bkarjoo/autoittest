import keyboard
from time import sleep

def control_a():
    keyboard.press_and_release('ctrl+a')


def control_c():
    keyboard.press_and_release('ctrl+c')


def control_v():
    keyboard.press_and_release('ctrl+v')


def write(some_string):
    keyboard.write(some_string)


def up_arrow():
    keyboard.press_and_release('up')
    sleep(.05)


def down_arrow():
    keyboard.press_and_release('down')
    sleep(.05)


def delete():
    keyboard.press_and_release('delete')
    sleep(.05)
