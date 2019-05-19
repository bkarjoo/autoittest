from mouse_movement import *
from pixel_info import *
from time import sleep

def find_launcher_window():
    # moves the mouse to the edge of the launcher window
    # pre-condition: the launcher window is the upper left window
    # there's no window behind it
    # there's at least a pixel of space between the edge and the launcher window
    set_image()
    for i in range(0,100):
        print get_color((i,i));
    while (True):
        print mouse_position()
        sleep(1)


find_launcher_window()
