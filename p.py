import pyautogui
import time
from pixel_color import *
import keyboard

def move_mouse(p):
    pyautogui.moveTo(p[0],p[1])

def get_first_windows_point():
    for x in range(1,1000):
        p = (x,x)
        if get_color(p) != 0: return p

def is_top_of_window(p):
    # it's top if left and right are not 0 and above is 0
    above = (p[0],p[1]-1)
    left = (p[0]-1,p[1])
    right = (p[0]+1,p[1])
    if p[1] == 1 and p[0] == 1:
        return get_color((1,1)) != 0
    elif p[1] == 1:
        return get_color(left) != 0 and get_color(right) != 0
    elif p[0] == 1:
        return get_color(above) == 0
    else:
        return get_color(above) == 0 and get_color(left) != 0 and get_color(right) != 0

def get_window_corner(p):
    if is_top_of_window(p):
        # loop left
        #print 1
        while True:
            p = (p[0]-1,p[1])
            if get_color(p) == 0: return (p[0]+1,p[1])
            if p[0] == 0: return (1,p[1])
    else:
        # loop up
        while True:
            p = (p[0],p[1]-1)
            if get_color(p) == 0: return (p[0],p[1]+1)
            if p[1] == 0: return (p[0],1)


def get_launcher_button_level(corner):
    # find the first window point
    p = corner
    button_level = (p[0]+30,p[1]+50)
    return button_level



def get_launcher_button(corner, which_button):
    p = get_launcher_button_level(corner)
    offset = (which_button-1) * 55
    return (p[0] + offset, p[1])

def loop_through_buttons(corner):
    p = get_launcher_button_level(corner)
    for r in range(0,12):
        p = (p[0] + 55, p[1])
        move_mouse(p)
        time.sleep(.5)

def single_click(point):
    move_mouse(point)
    pyautogui.click()

def double_click(point):
    move_mouse(point)
    pyautogui.click(clicks=2)

def find_window_edge():
    for x in range(1,1000,10):
        if get_color((x,500)) != 0: break
    for i in range(x,0,-1):
        if get_color((i,500)) == 0: return (i+1,500)
    # finds first window from mid screen

def get_corner_from_edge(edge):
    p = edge
    ini_color = get_color(p)
    #print p, ini_color
    while True:
        p = (p[0],p[1]-1)
        if p[1] == 0: return p(p[0],1)
        if get_color(p) != ini_color: return (p[0], p[1]+1)

def get_lower_corner(edge):
    p = edge
    ini_color = get_color(p)
    while True:
        p = (p[0],p[1]+50)
        if p[1] > 1000: return (p[0],1000)
        if get_color(p) == 0: break
    while True:
        p = (p[0],p[1]-10)
        if get_color(p) != 0: break
    while True:
        p = (p[0],p[1]+1)
        if p[1] > 1000: return (p[0],1000)
        if get_color(p) == 0: break
    return (p[0],p[1]-1)

def get_upper_corner(edge):
    p = get_lower_corner(edge)
    return (p[0],p[1]-743)

def get_open_button(upper_corner):
    return (upper_corner[0]+1075,upper_corner[1]+712)

def open_box(folder,box):
    launcher_corner = get_window_corner(get_first_windows_point())
    launcher_open_button = get_launcher_button(launcher_corner, 2)
    double_click(launcher_open_button)
    time.sleep(.1)
    open_dialog_edge = find_window_edge()
    open_dialog_corner = get_upper_corner(open_dialog_edge)
    for i in range(0,folder-1):
        keyboard.press_and_release('down')
        time.sleep(.01)
    keyboard.press_and_release('tab')
    keyboard.press_and_release('tab')
    for i in range(0,box-1):
        keyboard.press_and_release('down')
        time.sleep(.01)
    open_button = get_open_button(open_dialog_corner)
    double_click(open_button)
    time.sleep(.1)
    keyboard.press_and_release('space')

def run_back_test():
    launcher_corner = get_window_corner(get_first_windows_point())
    play_button = get_launcher_button(launcher_corner, 6)
    double_click(play_button)
    time.sleep(.1)

def confirm_windows_closed():
    # windows is closed if the desktop is black upto 1000
    pass

def open_setting_window():
    launcher_corner = get_window_corner(get_first_windows_point())
    setting_button = get_launcher_button(launcher_corner, 10)
    double_click(setting_button)
    time.sleep(.1)

def find_setting_window_corner():
    # get lower edge of launcher_corner
    launcher_corner = get_window_corner(get_first_windows_point())
    p = (launcher_corner[0],launcher_corner[1]+300)
    # horizantal scan
    while True:
        p = (p[0]+10,p[1])
        if get_color(p) != 0: break
    while True:
        p = (p[0]-1,p[1])
        if get_color(p) == 0: break
    p = (p[0]+1,p[1])

    # vertical scan
    edge_color = get_color(p)
    while True:
        p = (p[0],p[1]-10)
        if p[1] < 1: break
        if get_color(p) != edge_color: break
    while True:
        p = (p[0],p[1]+1)
        if get_color(p) == edge_color:break
    return p

def get_backtesting_tab(setting_window_corner):
    # given upper left corner offsets to backtesting tab
    return (setting_window_corner[0]+350,setting_window_corner[1]+45)

def get_one_day_radio_button(setting_window_corner):
    return (setting_window_corner[0]+30,setting_window_corner[1]+75)

def get_date_drop_down_button(setting_window_corner):
    return (setting_window_corner[0]+297,setting_window_corner[1]+75)

def get_date_picker(setting_window_corner):
    return (setting_window_corner[0]+197,setting_window_corner[1]+100)

def get_month_point(setting_window_corner, month):
    edge = setting_window_corner[0]
    top = setting_window_corner[1]
    first_month_row = top + 135
    month_row_step = 38
    first_month_column = edge + 125
    month_column_step = 46
    x = first_month_row
    y = first_month_column
    m = month


    if m >= 5 and m <= 8:
        x += month_row_step
    elif m >= 9:
        x += month_row_step * 2

    if m in (2,6,10):
        y += month_column_step
    elif m in (3,7,11):
        y += month_column_step * 2
    elif m in (4,8,12):
        y += month_column_step * 3

    return (y,x)

def change_backtesting_date(date):
    # date in yyyy-mm-dd format
    # open backtesting window
    open_setting_window()
    time.sleep(.01)
    corner = find_setting_window_corner()
    # open backtesting tab
    backtesting_tab = get_backtesting_tab(corner)
    double_click(backtesting_tab)
    time.sleep(.01)
    # choose one day radio button
    radio_button = get_one_day_radio_button(corner)
    double_click(radio_button)
    time.sleep(.01)
    # click down arrow
    drop_down = get_date_drop_down_button(corner)
    single_click(drop_down)
    time.sleep(.01)
    # year range pick
    date_picker = get_date_picker(corner)
    single_click(date_picker)
    # prep the date str
    the_date = date.split('-')
    year = the_date[0]
    month = int(the_date[1])
    day = the_date[2]
    # month pick
    month_point = get_month_point(corner, month)
    single_click(month_point)
    # day pick
    day_point = (corner[0]+220,corner[1]+78)
    double_click(day_point)
    keyboard.write(day)
    # year pick
    year_point = (corner[0]+245,corner[1]+78)
    single_click(year_point)
    keyboard.write(year)
    # save
    save_button = (corner[0]+515, corner[1]+458)
    single_click(save_button)
    pass

# launcher_corner = get_window_corner(get_first_windows_point())
# launcher_open_button = get_launcher_button(launcher_corner, 2)
#
#
#
#
# folder = 40
# box = 88
# open_box(folder,box)
# time.sleep(.1)
# run_back_test()
change_backtesting_date('2011-04-22')
