def convert_file_to_string(file_name):
    handle = open("pp/" + file_name + '.i')
    s = handle.read()
    return s


def grab_ael_price_increment():
    return convert_file_to_string('ael_price_increment')


def grab_ael_price():
    return convert_file_to_string('ael_price')


def grab_ael_time_increment():
    return convert_file_to_string('ael_time_increment')


def grab_ael_trigger():
    return convert_file_to_string('ael_trigger')


def grab_entry_order_limit():
    return convert_file_to_string('entry_order_limit')


def grab_entry_order_stop():
    return convert_file_to_string('entry_order_stop')


def grab_entry_trigger():
    return convert_file_to_string('entry_trigger')


def grab_position_sizing():
    return convert_file_to_string('position_sizing')


def grab_stop_price():
    return convert_file_to_string('stop_price')


def grab_target_limit():
    return convert_file_to_string('target_limit')


def grab_trail_how():
    return convert_file_to_string('trail_how')


def grab_trail_increment():
    return convert_file_to_string('trail_increment')


def grab_trail_trigger():
    return convert_file_to_string('trail_trigger')


def grab_basket_rules():
    return convert_file_to_string('basket_rules')
