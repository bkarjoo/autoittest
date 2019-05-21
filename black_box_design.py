from keyboard_clicks import *
from mouse_movement import *
from clipboard import *
from pixel_info import *
from launcher import *
from time import sleep
from code_grab import *

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
edit_entry_rule_button_offset = (900,310)
first_entry_order_selection_offset = (400,445)
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
expression_builder_formula_box_offset = (400,300)
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


def black_box_design_offset_clicker(offset):
    mouse_click_at((black_box_design_corner[0] + offset[0], black_box_design_corner[1] + offset[1]))


def cancel_black_box_design():
    black_box_design_offset_clicker(cancel_offset)


def validate_and_close_black_box_design():
    black_box_design_offset_clicker(validate_and_close_offset)


def add_new_exit_stop_order():
    black_box_design_offset_clicker(add_new_exit_stop_order_offset)


def edit_exit_stop_order():
    black_box_design_offset_clicker(edit_exit_stop_order_offset)


def add_new_exit_limit_order():
    black_box_design_offset_clicker(add_new_exit_limit_order_offset)


def edit_exit_limit_order():
    black_box_design_offset_clicker(edit_exit_limit_order_offset)


def add_new_entry_order():
    black_box_design_offset_clicker(add_new_entry_order_offset)


def edit_entry_order():
    black_box_design_offset_clicker(edit_entry_order_offset)


def edit_limit_price():
    # after opening the add/edit order form you need to click this button to edit limit price
    black_box_design_offset_clicker(edit_limit_price_offset)


def click_expression_builder_formula_box():
    black_box_design_offset_clicker(expression_builder_formula_box_offset)


def set_expression_builder_code(code):
    click_expression_builder_formula_box()
    set_clipboard_text(code)
    control_v()
    black_box_design_offset_clicker(expression_builder_ok_button_offset)


def set_order_form_destination():
    # sets the destination to CSFB
    black_box_design_offset_clicker(expression_builder_destination_offset)
    # press up 20 times
    for _ in range(0,20): up_arrow()
    # press down 13 times
    for _ in range(0,13): down_arrow()


def press_order_form_save():
    black_box_design_offset_clicker(order_form_save_offset)


# public API starts here -------------------------------------------------------------
# box meta data
def set_black_box_name(name):
    pass


def set_black_box_description(text):
    pass


def trigger_permit_backtesting():
    pass


def set_black_box_side(side_str):
    # LONG or SHORT
    pass


def set_black_box_scheme(scheme_str):
    # PlainVanilla or OPG
    pass


def trigger_use_strict_mode():
    pass


def trigger_enter_on_trigger(trigger_point):
    # BID ASK SNAPSHOT or NEW_MINUTE
    pass


def set_entry_trigger_rule(rule_str):
    # click edit entry rule button
    # clear the expression
    # click text area
    # paste rule_str
    # press ok
    pass

# entry -----------------------------------------------------------------------
def set_entry_order_limit_price():
    # click expression builder
    # click clear
    # click text area
    # paste rule_str
    # press ok
    pass


def set_entry_order_stop_price():
    # click expression builder
    # click clear
    # click text area
    # paste rule_str
    # press ok
    pass


def add_new_edit_order():
    # click add new order
    # call edit  entry order limit price
    # set order type
    # set order side
    # set destination
    # set size
    # set tif
    # set tif seconds
    pass


def edit_existing_entry_order():
    # assumes only limit price will be changed
    # select the first order
    # click edit order
    # call set_entry_order_limit_price
    pass


# target and ael -----------------------------------------------------------
def add_new_exit_limit_order():
    pass

def edit_existing_limit_order():
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
