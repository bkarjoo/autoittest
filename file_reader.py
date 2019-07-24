


def grab_code(which_code):
    return read_file('pp/' + which_code + '.i')


def read_file(path):
    f = open(path, 'r')
    s = f.read()
    f.close()
    return s
