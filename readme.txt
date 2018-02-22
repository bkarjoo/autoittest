required files to run backtesting

live_runs.csv (copy and paste)
box_mapping.csv (one for each server, only when they change)

liveruns has date and name (for faster results sort by date)
box_mapping has the box_name, folder, and box number

run all the backtests python p.py
throttle the speed, add only 1 test per second

liveruns are then imported into sql
backtest runs are also imported into sql

sql database is accessible via webserver
asp.net application provides dropdowns to construct a query

# list of all functions

# basic mouse control
move_mouse(p)
single_click(point)
double_click(point)

# to find the launcher window
get_first_windows_point()
is_top_of_window(p)
get_window_corner(p)
get_launcher_button_level(corner)
get_launcher_button(corner, which_button)

# running back test
find_window_edge()
get_corner_from_edge(edge)
get_lower_corner(edge)
get_upper_corner(edge)
get_open_button(upper_corner)
open_box(folder,box)
run_back_test()
confirm_windows_closed()

# changing date
open_setting_window()
find_setting_window_corner()
get_backtesting_tab(setting_window_corner)
get_one_day_radio_button(setting_window_corner)
get_date_drop_down_button(setting_window_corner)
get_date_picker(setting_window_corner)
get_month_point(setting_window_corner, month)
change_backtesting_date(date)
