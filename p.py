import pyautogui
import time
import keyboard
import pyperclip
from box_name_importer import *
import csv
from PIL import ImageGrab
import sys

confirm = False

long_delay = 2.5
extra_delay = 30
debug_print = False
debug_print_2 = True

def move_mouse(p):
    if debug_print: print 'moving mouse to: ', p
    if p == None: return
    if p[0] > 0 and p[1] > 0:
        pyautogui.moveTo(p[0],p[1])


def get_color(p,image):
    try:
        p = (p[0]-1,p[1]-1)
        return image.getpixel(p)
    except:
        return (-1,-1,-1)


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


def single_click(point):
    # move mouse to the point first then click
    move_mouse(point)
    pyautogui.click()


def double_click(point):
    # two single clicks with delay in between is more accurate
    # than requesting pyautogui clicks=2
    move_mouse(point)
    pyautogui.click(clicks=1)
    time.sleep(.1)
    pyautogui.click(clicks=1)


def find_window_edge():
    image = ImageGrab.grab()

    for y in range(300,800,50):
        for x in range(1,1000,1):
            if get_color((x,y),image) != (0,0,0):
                return (x,y)
    return None


def get_corner_from_edge(edge):
    if debug_print: print 'debug:','get_corner_from_edge'
    image = ImageGrab.grab()
    p = edge
    ini_color = get_color(p, image)
    #print p, ini_color
    while True:
        p = (p[0],p[1]-1)
        if p[1] == 0: return (p[0],1)
        if get_color(p, image) != ini_color: return (p[0], p[1]+1)


def get_open_window_height(corner):
    image = ImageGrab.grab()
    height = 0
    while get_color((corner[0],corner[1] + height), image) != (0,0,0):
        height += 1
    print 'height:', height


def is_job_successfully_added_windows(corner):
    # this is the smallest window
    # it is 145 pixels tall
    # so 145 pixels lower than it's corner should be black
    image = ImageGrab.grab()
    height = 146
    return get_color((corner[0],corner[1]+ height), image) == (0,0,0)


def is_settings_window(corner):
    image = ImageGrab.grab()
    height = 484
    move_mouse((corner[0],corner[1] + height))
    if debug_print: print 'color',get_color((corner[0],corner[1] + height), image)
    return get_color((corner[0],corner[1] + height), image) == (0,0,0) \
        and not is_job_successfully_added_windows(corner)


def is_open_blackbox_window(corner):
    image = ImageGrab.grab()
    height = 746
    return get_color((corner[0],corner[1] + height), image) == (0,0,0) \
        and not is_job_successfully_added_windows(corner) \
        and not is_settings_window(corner)


def is_blackbox_definition_windows(corner):
    image = ImageGrab.grab()
    height = 978
    return get_color((corner[0],corner[1] + height), image) == (0,0,0)  \
        and not is_job_successfully_added_windows(corner) \
        and not is_settings_window(corner) \
        and not is_open_blackbox_window(corner)


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

def is_clear():
    # if debug_print: print 'debug:','is_clear'
    # returns true if there's no open windows under the launcher, false otherwise
    image = ImageGrab.grab()
    for x in range(10,1280,50):
        for y in range (300, 750, 50):
            p = (x,y)
            c = get_color(p,image)
            if not c == (0,0,0):
                return False

    return True


def get_open_box_name():
    if debug_print: 'In get_open_box_name'
    edge = find_window_edge()
    corner = get_corner_from_edge(edge)
    if not is_blackbox_definition_windows(corner):
        x = raw_input("There's a window open but it's not a black box definition.")
    black_box_name_textbox = (corner[0]+200, corner[1]+70)
    single_click(black_box_name_textbox)
    time.sleep(.1)
    keyboard.press_and_release('ctrl+a')
    keyboard.press_and_release('ctrl+c')
    time.sleep(.05)
    box_name = pyperclip.paste()
    if debug_print: 'Exiting get_open_box_name', box_name
    return box_name


def open_box(folder,box, box_name):
    if debug_print: print 'debug:','open_box'
    if debug_print: print 'open_box', folder, box
    launcher_corner = get_window_corner(get_first_windows_point())
    launcher_open_button = get_launcher_button(launcher_corner, 2)
    if debug_print: print 'opening tree -- long delay', long_delay
    time.sleep(long_delay)

    if debug_print_2: print '--opening tree'
    i = 0
    while (is_clear()):
        i += 0;
        if i == 10:
            x = raw_input("ERROR : Tree didn't open")
        double_click(launcher_open_button)
        time.sleep(.1)

    open_dialog_edge = find_window_edge()
    open_dialog_corner = get_upper_corner(open_dialog_edge)

    verify = is_open_blackbox_window(open_dialog_corner)
    if verify:
        if debug_print: print "Open Black Box Tree is Open."
    else:
        x = raw_input("Open blackbox tree failed to open.")
    if debug_print_2: print '--tree opened'


    if debug_print: print 'foldering down -- long delay', long_delay
    time.sleep(long_delay)
    for i in range(0,folder-1):
        keyboard.press_and_release('down')
        time.sleep(.075)
    time.sleep(.05)
    keyboard.press_and_release('tab')
    time.sleep(.05)
    keyboard.press_and_release('tab')
    time.sleep(.05)
    if debug_print_2: print '--folder found'
    if debug_print: print 'boxing down -- long delay', long_delay
    time.sleep(long_delay)
    for i in range(0,box-1):
        keyboard.press_and_release('down')
        time.sleep(.075)
    time.sleep(.05)
    if debug_print_2: print '--box found'
    if debug_print: print 'opening box -- long delay', long_delay
    time.sleep(long_delay)
    if debug_print_2: print '--pressing open to open the box'
    open_button = get_open_button(open_dialog_corner)


    double_click(open_button)

    blackbox_edge = None
    i = 0
    while blackbox_edge == None:
        blackbox_edge = find_window_edge()
        time.sleep(.1)
        i += 1
        if i >= 10:
            x = raw_input("can't find blackbox edge")
    blackbox_corner = get_corner_from_edge(blackbox_edge)
    time.sleep(.1)
    verify = is_blackbox_definition_windows(blackbox_corner)
    if verify:
        if debug_print: print "blackbox is Open."
    else:
        if debug_print_2: print '--attempt 2'
        time.sleep(1)
        new_edge = find_window_edge()
        print 'new_edge', new_edge
        new_corener = get_corner_from_edge(new_edge)
        print new_corener
        new_is_open = is_blackbox_definition_windows(new_corener)
        print new_is_open
        if not new_is_open:
            if debug_print_2: print '--failed'
            new_edge = find_window_edge()
            print 'new_edge', new_edge
            new_corener = get_corner_from_edge(new_edge)
            print new_corener
            new_is_open = is_blackbox_definition_windows(new_corener)
            print new_is_open
            x = raw_input("Blackbox failed to open.")

    if debug_print_2: print '--black box is opened'
    found_name = get_open_box_name()
    if found_name != box_name:
        print found_name
        print box_name
        time.sleep(1)
        if get_open_box_name() != box_name:
            x = raw_input("There's a box open but it's not {}. Exit and fix box_loc.csv.".format(box_name))

    if debug_print_2: print '--verified box found: ', found_name
    if debug_print_2: print '--closing box'
    if debug_print: print 'closing box -- long delay', long_delay
    time.sleep(long_delay)

    i = 0
    while not is_clear():
        i += 1;
        if i == 10:
            close_any_window()
            time.sleep(.2)
            if not is_clear():
                x = raw_input("Box didn't close")
            break
        mouse_location = (blackbox_corner[0]+60,blackbox_corner[1]+940)
        print 'potentially error causing coordinates: ', mouse_location
        move_mouse(mouse_location)
        pyautogui.click()
        time.sleep(.1)

    if debug_print_2: print '--box closed'




def run_back_test():
    if debug_print_2: print '--pressing play'
    launcher_corner = get_window_corner(get_first_windows_point())
    play_button = get_launcher_button(launcher_corner, 6)
    double_click(play_button)
    time.sleep(.1)
    if debug_print_2: print '--pressed play'


def confirm_windows_closed():
    # windows is closed if the desktop is black upto 1000
    pass


def open_setting_window():
    if debug_print: print 'debug:','open_setting_window'
    launcher_corner = get_window_corner(get_first_windows_point())
    setting_button = get_launcher_button(launcher_corner, 10)
    double_click(setting_button)
    time.sleep(.1)
    i = 0
    while (is_clear()):
        i += 0;
        if i == 10:
            x = raw_input("Settings window didn't open")
        double_click(setting_button)
        time.sleep(.1)

    if debug_print: print 'checking if settings window is open'
    edge = find_window_edge()
    corner = get_corner_from_edge(edge)
    verify = is_settings_window(corner)
    if (verify):
        if debug_print: print 'settings window is open'
    else:
        x = raw_input("There's an open window but it's not settings window")
    return corner



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
    corner = open_setting_window()
    # open backtesting tab

    backtesting_tab = get_backtesting_tab(corner)
    double_click(backtesting_tab)
    time.sleep(.1)

    # choose one day radio button
    radio_button = get_one_day_radio_button(corner)
    double_click(radio_button)
    time.sleep(.1)
    if confirm:
        print 'RADIO BUTTON'
        time.sleep(1)

    # click down arrow
    drop_down = get_date_drop_down_button(corner)
    single_click(drop_down)
    time.sleep(.1)
    if confirm:
        print 'DOWN ARROW'
        time.sleep(1)

    # year range pick
    date_picker = get_date_picker(corner)
    single_click(date_picker)


    time.sleep(.1)
    if confirm:
        print 'DATE PICKER'
        time.sleep(1)

    # prep the date str
    the_date = date.split('-')
    year = the_date[0]
    month = int(the_date[1])
    day = the_date[2]
    # month pick
    month_point = get_month_point(corner, month)
    single_click(month_point)
    time.sleep(.1)

    if confirm:
        print 'MONTH POINT'
        time.sleep(1)
    # day pick
    day_point = (corner[0]+220,corner[1]+78)
    double_click(day_point)
    time.sleep(.1)

    if confirm:
        print 'MONTH POINT'
        time.sleep(1)

    keyboard.write(day)
    time.sleep(.1)
    keyboard.write(day)


    if confirm:
        print 'KEYBOARD WRITE DAY', day
        input('type something')
        time.sleep(1)

    # year pick
    year_point = (corner[0]+245,corner[1]+78)
    single_click(year_point)
    time.sleep(.1)
    keyboard.write(year)
    time.sleep(.1)
    # save
    save_button = (corner[0]+515, corner[1]+458)

    i = 0
    while not is_clear():
        single_click(save_button)
        time.sleep(.1)
        i += 1
        if i >= 10: break


def load_live_runs():
    try:
        with open('live_runs.csv') as csvDataFile:
            csvReader = csv.reader(csvDataFile)
            for row in csvReader:
                print row[0],row[1]
    except Exception as e:
        print e


def close_any_window():
    edge = find_window_edge()
    single_click(edge) # so window comes to focus
    time.sleep(.1)
    image = ImageGrab.grab()
    color = get_color(edge, image)

    while True:
        # go to corner
        edge = (edge[0],edge[1]-1)
        if edge[1] >= 0:
            if get_color(edge, image) != color:
                edge = (edge[0], edge[1]+1)

                break # edge is now the corner
        else:
            # out of bounds
            return


    print get_color(edge, image)
    while True:
        # go to upper right corner
        edge = (edge[0]+1,edge[1])
        if edge[1] < 1280:
            if get_color(edge, image) != color:
                edge = (edge[0]-1, edge[1])
                break # edge is now the upper corner
        else:
            # out of bounds
            return
    single_click((edge[0]-10,edge[1]+10))
    time.sleep(.1)




def run_tests(whichQuant = 1):



    # takes csv list with two columns date, box_name
    # TODO Load box mapping
    create_in_mem_db()
    create_box_loc_table()
    load_box_loc_csv()
    # TODO Read List
    theDate = ''

    with open('live_runs.csv') as liveRunFile:
        liveRunRows = csv.reader(liveRunFile)
        for row in liveRunRows:
            if debug_print_2: print row
            try:
                if debug_print: print 'looking for box -- long delay', long_delay
                time.sleep(long_delay)
                # x = raw_input('fetching box details for box {} in quant {}'.format(row[1], whichQuant))
                box_add = get_box_address(row[1],whichQuant)
                if debug_print_2: print 'get_box_address results: ', box_add
                if debug_print: print row[1], box_add
                if debug_print: print row[0]

                print 'starting date: ', row[0], 'box: ', row[1]
                if row[0] != theDate:
                    if debug_print_2: print 'set date to: ', row[0]
                    if debug_print: print 'setting date to', row[0]
                    time.sleep(long_delay)
                    # x = raw_input('setting date to {}'.format(row[0]))
                    theDate = row[0]
                    change_backtesting_date(theDate)

                    # prmpt = 'Was date set correctly? (y/n) to: {}'.format(theDate)
                    # raw_input('set date')


                # x = raw_input('opening box')
                if debug_print: print 'calling open_box'
                if debug_print_2: print 'open_box call'
                open_box(box_add[0],box_add[1],row[1])


                if debug_print_2: print 'making sure black box closed'
                i = 1
                while True:
                    if is_clear(): break
                    i += 1
                    if i > 10:
                        close_any_window()
                        if not is_clear():
                            x = raw_input('black box didnt close.')
                        break
                    time.sleep(.1)
                if debug_print_2: print 'box closed'

                # x = raw_input('running back test')
                if debug_print: print 'running back test -- long delay', long_delay
                time.sleep(long_delay)
                if debug_print_2: print 'run_back_test call'
                run_back_test()
                time.sleep(.1)


                # verify job_successfully_added_window is open
                if debug_print_2: print 'check small window opened'
                i = 1
                while is_clear():
                    time.sleep(.2)
                    i+=1
                    if i == 10:
                        x = raw_input("small window didn't open")

                job_successfully_added_window_edge = find_window_edge()
                jsaw_corner = get_corner_from_edge(job_successfully_added_window_edge)
                verify = is_job_successfully_added_windows(jsaw_corner)
                if verify:
                    if debug_print: print 'small window open'
                else:
                    x = raw_input("some window opened but small window didn't open")

                if debug_print_2: print 'small window opened'
                if debug_print_2: print 'closing small window'
                if debug_print: print 'closing small window -- long delay', long_delay
                time.sleep(long_delay)
                i = 1
                while not is_clear():
                    double_click((jsaw_corner[0]+260, jsaw_corner[1]+120))
                    i += 1
                    if i > 10:
                        close_any_window()
                        time.sleep(.2)
                        if not is_clear():
                            x = raw_input('small window didnt close.')
                        break
                    time.sleep(.1)
                if debug_print_2: print 'small window closed'
                if debug_print_2: print 'done with ', row

                if extra_delay > 0: time.sleep(extra_delay)
            except Exception as e:
                print 'Error', e
                break
        print "All Done."

which_quant = 1
if len(sys.argv) > 1:
    if sys.argv[1] == '2': which_quant = 2
run_tests(which_quant)
