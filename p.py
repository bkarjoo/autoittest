import pyautogui
import time
import keyboard
from box_name_importer import *
import csv
import ImageGrab

long_delay = .1
debug_print = True
#hi
def move_mouse(p):
    if p[0] > 0 and p[1] > 0:
        pyautogui.moveTo(p[0],p[1])


def get_color(p,image):
    p = (p[0]-1,p[1]-1)
    return image.getpixel(p)


def get_first_windows_point():
    # comes down from 1,1 diagonally, assumes the first window is in its diagonal path
    if debug_print: print 'debug:','get_first_windows_point'
    i = ImageGrab.grab()
    for x in range(1,1000):
        p = (x,x)
        if get_color(p,i) != (0,0,0): return p


def is_top_of_window(p, i):
    # it's top if left and right are not 0 and above is 0
    if debug_print: print 'debug:','is_top_of_window'


    # get above left and rigt
    if p[1] > 1:
        above = (p[0],p[1]-1)
    if p[0] > 1:
        left = (p[0]-1,p[1])
    if p[0] < i.size[0]:
        right = (p[0]+1,p[1])
    if p == (1, 1):
        # can't go left or up
        return get_color(p,i) != (0,0,0) and get_color(right,i) != (0,0,0)
    elif p[1] == 1:
        # can't go any higher, but we can go left and right
        return get_color(left,i) != (0,0,0) and get_color(right,i) != (0,0,0)
    elif p[0] == 1:
        # can't go any more left, but can go up and right
        return get_color(above,i) != (0,0,0) and get_color(right,i) != (0,0,0)
    else:
        # we can go left, right, and up
        return get_color(right,i) != (0,0,0) and get_color(left,i) != (0,0,0) and get_color(above,i) == (0,0,0)


def get_window_corner(p):
    # assumes you're at the edge, either top, or left side
    if debug_print: print 'debug:','get_window_corner'
    i = ImageGrab.grab()
    if is_top_of_window(p,i):
        # loop left to get to edge
        while True:
            if p[0] <= 1: return (1, p[1])
            p = (p[0]-1,p[1])
            if get_color(p,i) == (0,0,0):
                # retract one pixel to get back on the window
                return (p[0]+1,p[1])
    else:
        # loop up
        while True:
            if p[1] <= 1: return (p[0], 1)
            p = (p[0], p[1]-1)
            if get_color(p,i) == (0,0,0):
                # retract one pixel to get back on the window
                return (p[0],p[1]+1)


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
    pyautogui.click(clicks=1)
    time.sleep(.1)
    pyautogui.click(clicks=1)


def find_window_edge():
    image = ImageGrab.grab()
    for x in range(1,1000,10):
        if get_color((x,500),image) != (0,0,0): break
    for i in range(x,0,-1):
        if get_color((i,500),image) == (0,0,0): return (i+1,500)
    # finds first window from mid screen


def get_corner_from_edge(edge):
    if debug_print: print 'debug:','get_corner_from_edge'
    image = ImageGrab.grab()
    p = edge
    ini_color = get_color(p, image)
    #print p, ini_color
    while True:
        p = (p[0],p[1]-1)
        if p[1] == 0: return p(p[0],1)
        if get_color(p, image) != ini_color: return (p[0], p[1]+1)


def get_lower_corner(edge):
    if debug_print: print 'debug:','get_lower_corner'
    p = edge
    image = ImageGrab.grab()
    ini_color = get_color(p,image)
    while True:
        p = (p[0],p[1]+50)
        if p[1] > 1000: return (p[0],1000)
        if get_color(p,image) == (0,0,0): break
    while True:
        p = (p[0],p[1]-10)
        if get_color(p,image) != (0,0,0): break
    while True:
        p = (p[0],p[1]+1)
        if p[1] > 1000: return (p[0],1000)
        if get_color(p,image) == (0,0,0): break
    return (p[0],p[1]-1)


def get_upper_corner(edge):
    if debug_print: print 'debug:','get_upper_corner'
    p = get_lower_corner(edge)
    return (p[0],p[1]-743)


def get_open_button(upper_corner):
    return (upper_corner[0]+1075,upper_corner[1]+712)


def open_box(folder,box):
    if debug_print: print 'debug:','open_box'
    print 'open_box', folder, box
    launcher_corner = get_window_corner(get_first_windows_point())
    launcher_open_button = get_launcher_button(launcher_corner, 2)
    print 'opening tree -- long delay', long_delay
    time.sleep(long_delay)
    while is_clear():
        double_click(launcher_open_button)
        time.sleep(.25)
    open_dialog_edge = find_window_edge()
    open_dialog_corner = get_upper_corner(open_dialog_edge)

    print 'foldering down -- long delay', long_delay
    time.sleep(long_delay)
    for i in range(0,folder-1):
        keyboard.press_and_release('down')
        time.sleep(.075)
    time.sleep(.05)
    keyboard.press_and_release('tab')
    time.sleep(.05)
    keyboard.press_and_release('tab')
    time.sleep(.05)

    print 'boxing down -- long delay', long_delay
    time.sleep(long_delay)
    for i in range(0,box-1):
        keyboard.press_and_release('down')
        time.sleep(.075)
    time.sleep(.05)

    print 'opening box -- long delay', long_delay
    time.sleep(long_delay)
    open_button = get_open_button(open_dialog_corner)

    double_click(open_button)

    print 'closing box -- long delay', long_delay
    time.sleep(long_delay)
    move_mouse((200,940))
    time.sleep(.05)
    pyautogui.click()
    time.sleep(.05)
    keyboard.press_and_release('space')

    time.sleep(.1)
    i = 1

    print 'making sure box closed -- long delay', long_delay
    time.sleep(long_delay)
    while True:
        print ('waiting 142')
        if is_clear: break
        i += 1
        if i > 10:
            move_mouse((200,940))
            pyautogui.click()
            keyboard.press_and_release('space')
            break
        time.sleep(.1)


    # TODO : Confirm it's cosed by looking for black space under launcher


def run_back_test():
    launcher_corner = get_window_corner(get_first_windows_point())
    play_button = get_launcher_button(launcher_corner, 6)
    double_click(play_button)
    time.sleep(.1)


def confirm_windows_closed():
    # windows is closed if the desktop is black upto 1000
    pass


def open_setting_window():
    if debug_print: print 'debug:','open_setting_window'
    launcher_corner = get_window_corner(get_first_windows_point())
    setting_button = get_launcher_button(launcher_corner, 10)
    double_click(setting_button)
    time.sleep(.1)


def find_setting_window_corner():
    image = ImageGrab.grab()
    if debug_print: print 'debug:','find_setting_window_corner'
    # get lower edge of launcher_corner
    launcher_corner = get_window_corner(get_first_windows_point())
    p = (launcher_corner[0],launcher_corner[1]+300)
    # horizantal scan
    while True:
        p = (p[0]+10,p[1])
        if get_color(p,image) != (0,0,0): break
    while True:
        p = (p[0]-1,p[1])
        if get_color(p,image) == (0,0,0): break
    p = (p[0]+1,p[1])

    # vertical scan
    edge_color = get_color(p,image)
    while True:
        p = (p[0],p[1]-10)
        if p[1] < 1: break
        if get_color(p,image) != edge_color: break
    while True:
        p = (p[0],p[1]+1)
        if get_color(p,image) == edge_color:break
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


def load_live_runs():
    try:
        with open('live_runs.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                print row[0],row[1]
    except Exception as e:
        print e


def is_clear():
    if debug_print: print 'debug:','is_clear'
    # returns true if there's no open windows under the launcher, false otherwise
    image = ImageGrab.grab()
    for x in range(10,600,50):
        for y in range (300, 900, 50):
            p = (x,y)
            c = get_color(p,image)
            # print i,
            # if i == -1:
            #     time.sleep(1)
            #     keyboard.press_and_release('space')
            #     time.sleep(1)
            #     a = raw_input('whats going on?')
            #     return True
            if not c== (0,0,0):
                print ''
                return False

    print ''
    return True


def run_tests(whichQuant = 1):
    # takes csv list with two columns date, box_name
    # TODO Load box mapping
    create_in_mem_db()
    create_box_loc_table()
    load_box_loc_csv()
    # TODO Read List
    theDate = ''

    with open('live_runs.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            try:
                print 'looking for box -- long delay', long_delay
                time.sleep(long_delay)
                # x = raw_input('fetching box details for box {} in quant {}'.format(row[1], whichQuant))
                box_add = get_box_address(row[1],whichQuant)
                print row[1], box_add

                print row[0]
                if row[0] != theDate:
                    print 'setting date -- long delay', long_delay
                    time.sleep(long_delay)
                    # x = raw_input('setting date to {}'.format(row[0]))
                    theDate = row[0]
                    change_backtesting_date(theDate)
                    while not is_clear():
                        time.sleep(.1)

                # x = raw_input('opening box')
                print 'calling open_box'
                open_box(box_add[0],box_add[1])


                i = 1
                while True:
                    print 'waiting 314'
                    if is_clear(): break
                    i += 1
                    if i > 10: break
                    time.sleep(.1)

                # x = raw_input('running back test')
                print 'running back test -- long delay', long_delay
                time.sleep(long_delay)
                run_back_test()
                time.sleep(.2)


                print 'closing small window -- long delay', long_delay
                time.sleep(long_delay)
                i = 1
                while True:
                    print ('waiting 324')
                    if is_clear(): break
                    keyboard.press_and_release('space')
                    i += 1
                    if i > 10: break
                    time.sleep(.1)
                # x = raw_input('done')

                # x = raw_input('continue (y/n)')
                # if x == 'n':
                #     break
            except Exception as e:
                print 'Error', e
                x = raw_input('press a key to continue')




    # TODO set the date (if necessary)
    # TODO run the test
    pass

# launcher_corner = get_window_corner(get_first_windows_point())
# launcher_open_button = get_launcher_button(launcher_corner, 2)
#
# folder = 40
# box = 88
# open_box(folder,box)
# time.sleep(.1)
# run_back_test()
# change_backtesting_date('2011-04-22')

run_tests()

# print is_clear()
