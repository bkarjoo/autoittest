from keyboard_clicks import *
from mouse_movement import *
from clipboard import *
from pixel_info import *
from launcher import *
from time import sleep
from code_grab import *
import configparser

black_box_design_corner = (0,0)
# main black box design window offsets
black_box_name_offset = (200,65)
black_box_description_offset = (200,125)
black_box_side_offset = (200,200)
black_box_scheme_offset = (200,225)
use_strict_mode_offset = (100,270)
permit_back_testing_offset = (700,130) # permit live is left out
enter_on_bid_offset = (800,105)
enter_on_ask_offset = (800,130)
enter_on_snapshot_offset = (800,205)
enter_on_new_minute_offset = (800,230)
entry_trigger_text_box_offset = (400,410)
edit_entry_rule_button_offset = (900,310)
first_entry_order_offset = (400,445)
add_new_entry_order_offset = (920, 420)
edit_entry_order_offset = (920, 450)
first_exit_limit_order_offset = (400,625)
add_new_exit_limit_order_offset = (920, 605)
edit_exit_limit_order_offset = (920, 635)
first_stop_order_offset = (400,775)
add_new_exit_stop_order_offset = (920, 750)
edit_exit_stop_order_offset = (920, 780)
enable_stop_trailing_on_new_second_offset = (100,885)
cancel_offset = (70, 945)
validate_and_close_offset = (930,945)
# order form offsets
order_form_order_type_drop_down_offset = (380,305)
order_form_destination_drop_down_offset = (500,300)
order_form_side_offset = (300,330)
order_form_size_offset = (500,330)
order_form_edit_limit_price_offset = (750, 390)
order_form_edit_stop_price_offset = (750,470)
order_form_tif_drop_down_offset = (350,550)
order_form_tif_seconds_offset = (450,550)
order_form_cancel_offset = (650,720)
order_form_save_offset = (740,720)
# ael form offset
ael_form_edit_trigger_offset = (740,400)
ael_form_edit_trail_how_offset = (740,450)
ael_form_edit_time_increment_offset = (740,500)
ael_form_edit_price_increment_offset = (740,530)
ael_form_on_last_offset = (630,580)
ael_form_on_second_offset = (700,580)
ael_form_on_bid_ask_offset = (630,600)
ael_form_convert_to_stop_offset = (630,630)
# stop form offset
stop_form_common_order_tab_offset = (300,355)
stop_form_primus_stop_order_offset = (450,355)
stop_form_stop_price_edit_offset = (550,355)
stop_form_enable_trailing_check_box_offset = (300,460)
stop_form_edit_trail_trigger_offset = (750,490)
stop_form_edit_trail_how_offset = (750,560)
stop_form_edit_increment_offset = (750,630)
# expression builder offset
expression_builder_formula_text_area_offset = (400,300)
expression_builder_clear_button_offset = (780,430)
expression_builder_ok_button_offset = (920, 750)
# tabs
design_tab_offset = (30,30)
symbol_tab_offset = (70,30)
option_tab_offset = (130,30)
risk_management_tab_offset = (180,30)
launch_rule_tab_offset = (290,30)
# basket_rules
choose_basket_button_offset = (900,60)
basket_manager_private_tab_offset = (320,270)
basket_manager_second_folder_offset = (320,340)
basket_manager_right_click_point_offset = (520,340) # for building new boxes
basket_manager_right_click_menu_new_offset = (530, 350)
basket_manager_right_click_menu_edit_offset = (530, 370) #edit is not supported for now
basket_manager_basket_name_text_box_offset = (520,140)
basket_manager_basket_description_text_box_offset = (520,190)
basket_manager_activate_dynamic_basket_rules_offset = (320,260)
basket_manager_apply_dynamic_basket_to_all_symbols_offset = (520,260)
basket_manager_dynamic_rule_text_area_offset = (520,360)
basket_manager_symbols_text_area_offset = (520,460)
basket_manager_always_excluded_offset = (520,700)
basket_manager_htb_allowed_offset = (520,800)
basket_manager_save_button_offset = (900,140)
# options tab
use_time_options_check_box_offset = (70,75)
start_subscription_hour_offset = (175,110)
start_subscription_minute_offset = (190,110)
start_subscription_seconds_offset = (210,110)
start_subscription_AM_PM_offset = (220,110)
start_entering_positions_hour_offset = (175,145)
start_entering_positions_minute_offset = (190,145)
start_entering_positions_seconds_offset = (210,145)
start_entering_positions_AM_PM_offset = (220,145)
stop_entering_positions_hour_offset = (175,180)
stop_entering_positions_minute_offset = (190,180)
stop_entering_positions_seconds_offset = (210,180)
stop_entering_positions_AM_PM_offset = (220,180)
cancel_all_pending_orders_hour_offset = (175,220)
cancel_all_pending_orders_minute_offset = (190,220)
cancel_all_pending_orders_seconds_offset = (210,220)
cancel_all_pending_orders_AM_PM_offset = (220,220)
close_all_open_positions_hour_offset = (175,250)
close_all_open_positions_minute_offset = (190,250)
close_all_open_positions_seconds_offset = (210,250)
close_all_open_positions_AM_PM_offset = (220,250)
place_OPG_orders_hour_offset = (175,290)
place_OPG_orders_minute_offset = (190,290)
place_OPG_orders_seconds_offset = (210,290)
place_OPG_orders_AM_PM_offset = (220,290)
# position sizing
enable_position_sizing_scheme_check_box_offset = (120,350)
position_sizing_text_area_offset = (120,400)
# risk management
enable_black_box_risk_management_check_box_offset = (50,60)
maximum_order_shares_text_box_offset = (190,630)
# launch rules
enable_black_box_launch_rule_check_box_offset = (50,60)
launch_rule_text_area_offset = (100,300)


def find_window_edge():
    set_image()

    for y in range(300,800,50):
        for x in range(1,1000,1):
            if get_color((x,y)) != (0,0,0):
                return (x,y)
    return None


def get_corner_from_edge(edge):
    set_image()
    p = edge
    ini_color = get_color(p)
    #print p, ini_color
    while True:
        p = (p[0],p[1]-1)
        if p[1] == 0: return (p[0],1)
        if get_color(p) != ini_color: return (p[0], p[1]+1)


def open_black_box_design():
    open_new_box()
    sleep(1)
    edge = find_window_edge()
    corner = get_corner_from_edge(edge)


def click_offset_from_design_corner(offset):
    mouse_click_at((black_box_design_corner[0] + offset[0], black_box_design_corner[1] + offset[1]))


def cancel_black_box_design():
    click_offset_from_design_corner(cancel_offset)


def validate_and_close_black_box_design():
    click_offset_from_design_corner(validate_and_close_offset)


def add_new_exit_stop_order():
    click_offset_from_design_corner(add_new_exit_stop_order_offset)


def edit_exit_stop_order():
    click_offset_from_design_corner(edit_exit_stop_order_offset)


def add_new_exit_limit_order():
    click_offset_from_design_corner(add_new_exit_limit_order_offset)


def edit_exit_limit_order():
    click_offset_from_design_corner(edit_exit_limit_order_offset)


def add_new_entry_order():
    click_offset_from_design_corner(add_new_entry_order_offset)


def edit_entry_order():
    click_offset_from_design_corner(edit_entry_order_offset)


def edit_limit_price():
    # after opening the add/edit order form you need to click this button to edit limit price
    click_offset_from_design_corner(edit_limit_price_offset)


def click_expression_builder_formula_box():
    click_offset_from_design_corner(expression_builder_formula_box_offset)


def set_expression_builder_code(code):
    click_expression_builder_formula_box()
    set_clipboard_text(code)
    control_v()
    click_offset_from_design_corner(expression_builder_ok_button_offset)


def set_order_form_destination():
    # sets the destination to CSFB
    click_offset_from_design_corner(expression_builder_destination_offset)
    # press up 20 times
    for _ in range(0,20): up_arrow()
    # press down 13 times
    for _ in range(0,13): down_arrow()


def press_order_form_save():
    click_offset_from_design_corner(order_form_save_offset)


def confirm_design_box_is_open():
    # TODO implement
    pass


# box meta data
def set_black_box_name(name):
    # box is open already
    # tab one is selected already
    click_offset_from_design_corner(black_box_name_offset)
    set_clipboard_text(name)
    control_v()


def set_black_box_description(text):
    click_offset_from_design_corner(black_box_description_offset)
    set_clipboard_text(text)
    control_v()


def trigger_permit_backtesting():
    click_offset_from_design_corner(permit_back_testing_offset)


def set_black_box_side(side_str):
    # LONG or SHORT
    click_offset_from_design_corner(black_box_side_offset)
    if (side_str == 'LONG'):
        up_arrow()
    else:
        down_arrow()


def set_black_box_scheme(scheme_str):
    # PlainVanilla or OPG
    click_offset_from_design_corner(black_box_scheme_offset)
    if (scheme_str == 'OPG'):
        for _ in range(0,4): up_arrow()
        down_arrow()
    else:
        for _ in range(0,4): up_arrow()


def trigger_use_strict_mode():
    click_offset_from_design_corner(use_strict_mode_offset)


def trigger_enter_on_trigger(trigger_point):
    # BID ASK SNAPSHOT or NEW_MINUTE
    if trigger_point == 'BID':
        click_offset_from_design_corner(enter_on_bid_offset)
    elif trigger_point == 'ASK':
        click_offset_from_design_corner(enter_on_ask_offset)
    elif trigger_point == 'SNAPSHOT':
        click_offset_from_design_corner(enter_on_snapshot_offset)
    elif trigger_point == "NEW MINUTE":
        click_offset_from_design_corner(enter_on_new_minute_offset)

def trigger_enable_stop_trailing_on_new_second():
    click_offset_from_design_corner(enable_stop_trailing_on_new_second_offset)


def set_main_black_box_settings():
    # reads them from box_settings.properties file
    # assumes box is open
    # will overwrite what's already there
    props = configparser.RawConfigParser()
    props.read('box_settings.properties')
    prop_dict = dict(props.items('main'))

    set_black_box_name(prop_dict['box_name'])
    set_black_box_description(prop_dict['black_box_description'])
    trigger_permit_backtesting()
    set_black_box_side(prop_dict['black_box_side'])
    set_black_box_scheme(prop_dict['black_box_scheme'])
    if prop_dict['enter_on_last'] == 'FALSE': trigger_enter_on_trigger('LAST')
    if prop_dict['enter_on_bid'] == 'TRUE': trigger_enter_on_trigger('BID')
    if prop_dict['enter_on_ask'] == 'TRUE': trigger_enter_on_trigger('ASK')
    if prop_dict['enter_on_snapshot'] == 'TRUE': trigger_enter_on_trigger('SNAPSHOT')
    if prop_dict['enter_on_new_minute'] == 'TRUE': trigger_enter_on_trigger('NEW MINUTE')
    if prop_dict['enable_stop_trailing_on_new_second'] == 'TRUE': trigger_enable_stop_trailing_on_new_second()




# all orders common -----------------------------------------------------------
def set_order_type(type_str):
    # precondition: order form is open
    t = .4
    click_offset_from_design_corner(order_form_order_type_drop_down_offset)
    up_arrow()
    sleep(t)
    click_offset_from_design_corner(order_form_order_type_drop_down_offset)
    up_arrow()
    sleep(t)
    click_offset_from_design_corner(order_form_order_type_drop_down_offset)
    up_arrow()
    sleep(t)
    click_offset_from_design_corner(order_form_order_type_drop_down_offset)
    up_arrow()
    sleep(t)
    click_offset_from_design_corner(order_form_order_type_drop_down_offset)
    up_arrow()
    sleep(t)
    click_offset_from_design_corner(order_form_order_type_drop_down_offset)
    up_arrow()
    sleep(t)
    if type_str == 'LIMIT': return
    click_offset_from_design_corner(order_form_order_type_drop_down_offset)
    down_arrow()
    sleep(t)
    if type_str == 'STOP_MARKET': return
    click_offset_from_design_corner(order_form_order_type_drop_down_offset)
    down_arrow()
    sleep(t)
    if type_str == 'STOP_LIMIT': return
    click_offset_from_design_corner(order_form_order_type_drop_down_offset)
    down_arrow()
    sleep(t)
    if type_str == 'MARKET': return
    click_offset_from_design_corner(order_form_order_type_drop_down_offset)
    down_arrow()
    sleep(t)
    if type_str == 'PRIMUS_MARKET': return
    click_offset_from_design_corner(order_form_order_type_drop_down_offset)
    down_arrow()
    sleep(t)
    if type_str == 'PRIMUS_STOP': return
    click_offset_from_design_corner(order_form_order_type_drop_down_offset)
    down_arrow()
    sleep(t)


def set_order_side(side_str):
    click_offset_from_design_corner(order_form_side_offset)
    up_arrow()
    up_arrow()
    if side_str == 'BUY': return
    down_arrow()
    if side_str == "SELL": return
    down_arrow()


def set_order_destination(destination_str):
    click_offset_from_design_corner(order_form_destination_drop_down_offset)
    for _ in range(0,18): up_arrow()
    down_arrow()
    if destination_str == 'SDOT': return
    down_arrow()
    if destination_str == 'NSDQ': return
    down_arrow()
    if destination_str == 'ARCA': return
    down_arrow()
    if destination_str == 'BATS': return
    down_arrow()
    if destination_str == 'EDGA': return
    down_arrow()
    if destination_str == 'EDGX': return
    down_arrow()
    if destination_str == 'RASH': return
    down_arrow()
    if destination_str == 'NITE_FAN_A': return
    down_arrow()
    if destination_str == 'NITE_FAN_B': return
    down_arrow()
    if destination_str == 'BATSZ': return
    down_arrow()
    if destination_str == 'NQBX': return
    down_arrow()
    if destination_str == 'SIGMA': return
    down_arrow()
    if destination_str == 'CSFB': return
    down_arrow()
    if destination_str == 'CLRA': return
    down_arrow()
    if destination_str == 'CLRX': return
    down_arrow()
    if destination_str == 'CSFB_HIDDEN': return
    down_arrow()
    if destination_str == 'CSFB_SNIPER_P': return
    down_arrow()
    if destination_str == 'STEALTH': return


def set_order_size(size):
    click_offset_from_design_corner(order_form_size_offset)
    sleep(1)
    control_a()
    set_clipboard_text(size)
    control_v()


def set_order_tif(tif_str):
    # for limit and stop limit only
    click_offset_from_design_corner(order_form_tif_drop_down_offset)
    for _ in range(0, 10): up_arrow()
    if tif_str == 'TIF_IOC': return
    down_arrow()
    if tif_str == 'SECONDS': return
    down_arrow()
    if tif_str == 'TIF_NOW': return
    down_arrow()
    if tif_str == 'TIF_IOC_ON_OPEN': return
    down_arrow()
    if tif_str == 'TIF_IOC_ON_CLOSE': return
    down_arrow()
    if tif_str == 'TIF_PASSIVE_LIQUIDITY': return
    down_arrow()
    if tif_str == 'TIF_OPENING': return
    down_arrow()
    if tif_str == 'TIF_CLOSING_OFFSET': return
    down_arrow()
    if tif_str == 'TIF_ON_CLOSE': return
    down_arrow()
    if tif_str == 'TIF_MARKET_HOURS': return
    down_arrow()


def set_order_tif_seconds(seconds):
    click_offset_from_design_corner(order_form_tif_seconds_offset)
    control_a()
    set_clipboard_text(seconds)
    control_v()


def set_order_limit_price(rule_str):
    click_offset_from_design_corner(order_form_edit_limit_price_offset)
    sleep(1)
    click_offset_from_design_corner(expression_builder_clear_button_offset)
    click_offset_from_design_corner(expression_builder_formula_text_area_offset)
    set_clipboard_text(rule_str)
    control_v()
    click_offset_from_design_corner(expression_builder_ok_button_offset)


def set_order_stop_price(rule_str):
    click_offset_from_design_corner(order_form_edit_stop_price_offset)
    sleep(1)
    click_offset_from_design_corner(expression_builder_clear_button_offset)
    click_offset_from_design_corner(expression_builder_formula_text_area_offset)
    set_clipboard_text(rule_str)
    control_v()
    click_offset_from_design_corner(expression_builder_ok_button_offset)



# entry -----------------------------------------------------------------------
def set_entry_trigger_rule(rule_str):
    # click edit entry rule button
    click_offset_from_design_corner(entry_trigger_text_box_offset)
    # clear the expression
    control_a()
    # click text area
    delete()
    # paste rule_str
    set_clipboard_text(rule_str)
    control_v()


# this is called by build box command,
# takes a properties class AKA traits class
# takes a limit rule
# takes an optional stop rule
def add_new_edit_order(limit_rule, stop_rule = ''):
    # click add new order
    props = configparser.RawConfigParser()
    props.read('entry_order.properties')
    prop_dict = dict(props.items('main'))

    click_offset_from_design_corner(add_new_entry_order_offset)
    sleep(1)
    set_order_tif(prop_dict['tif'])
    sleep(.1)
    set_order_tif_seconds(prop_dict['tif_seconds'])

    set_order_limit_price(limit_rule)
    sleep(1)

    set_order_type(prop_dict['order_type'])
    set_order_side(prop_dict['order_side'])
    set_order_destination(prop_dict['destination'])
    set_order_size(prop_dict['size'])

    if stop_rule != '': set_order_stop_price(stop_rule)
    sleep(1)
    click_offset_from_design_corner(order_form_save_offset)


def edit_existing_entry_order(limit_rule, stop_rule=''):
    # assumes only limit price will be changed
    # select the first order
    # click edit order
    # call set_entry_order_limit_price
    click_offset_from_design_corner(first_entry_order_offset)
    sleep(.1)
    click_offset_from_design_corner(first_entry_order_offset)
    set_order_limit_price(limit_rule)
    sleep(1)
    set_order_stop_price(stop_rule)
    sleep(1)
    click_offset_from_design_corner(order_form_save_offset)


# target and ael -----------------------------------------------------------
def add_new_exit_limit_order(limit_price):
    click_offset_from_design_corner(add_new_exit_limit_order_offset)
    sleep(1)

add_new_exit_limit_order()


def add_new_ael_order():
    pass


def edit_existing_limit_order():
    pass


def edit_existing_ael_limit_order():
    pass


# stop loss order ----------------------------------------------------------
def add_new_stop_loss_order():
    pass

def edit_existing_stop_loss_order():
    pass

# basket -------------------------------------------------------------------
def create_basket():
    pass

def edit_basket():
    pass

# time options ---------------------------------------------------------------
def set_time_options():
    pass

# position sizing ----------------------------------------------------------
def set_position_sizing():
    # enable strict mode
    # add max order shares in risk management
    pass

# launch rules ----------------------------------------------------------
def set_launch_rules():
    # another option for controlling back tests
    # although setting calendars is easier
    pass
