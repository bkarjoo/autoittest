from mouse_movement import *
from pixel_info import *

launcher_corner = (0,0)

def first_window_corner():
    # first window that appears if you traverse diagnoally from upper left corner
    set_image()
    i = 0
    for i in range(0,100):
        color = get_color((i,i));
        if color != (-1,-1,-1) and color != (0,0,0): break

    # you've hit either top edge or left edge
    x = y = i

    if get_color((x-1, y)) == (0,0,0):
        #left edge move up
        while get_color((x, y)) != (0,0,0) and get_color((x,y)) != (-1,-1,-1):
            y -= 1
            if y == 0:  break
        y += 1

    elif get_color((x, y-1)) == (0,0,0):
        # top edge move left
        while get_color((x, y)) != (0,0,0) and get_color((x,y)) != (-1,-1,-1):
            x -= 1
            if x == 0: break
        x += 1

    return (x,y)

def set_launcher_window_corner():
    # moves the mouse to the edge of the launcher window
    # pre-condition: the launcher window is the upper left window
    # there's no window behind it
    # there's at least a pixel of space between the edge and the launcher window
    global launcher_corner
    launcher_corner = first_window_corner()

def get_launcher_button_level(corner):
    # finds the middle of the launcher's button row
    # find the first window point
    p = corner
    button_level = (p[0]+30,p[1]+50)
    return button_level

def get_launcher_button(corner, which_button):
    # takes the corner of the launcher windows
    # which_button is the button number, 1 being leftmost button
    p = get_launcher_button_level(corner)
    offset = (which_button-1) * 55
    return (p[0] + offset, p[1])

def test_loop_through_buttons(corner):
    # for testing only
    p = get_launcher_button_level(corner)
    for r in range(0,12):
        p = (p[0] + 55, p[1])
        move_mouse(p)
        time.sleep(.5)

def open_new_box():
    # open new box
    move_mouse(get_launcher_button(launcher_corner, 1))
    mouse_double_click()
