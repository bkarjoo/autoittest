from ctypes import windll

def get_color(p):
    hdc = windll.user32.GetDC(0)
    color = windll.gdi32.GetPixel(hdc, p[0], p[1])
    return color

# print get_color((100,100))
