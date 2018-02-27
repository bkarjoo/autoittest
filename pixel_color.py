# from ctypes import *
#
# def get_color(p):
#     windll.user32.GetDC.restype = c_void_p
#     hdc = windll.user32.GetDC(None)
#     print hdc
#     color = windll.gdi32.GetPixel(hdc, p[0], p[1])
#     return color
import ImageGrab

image = 0

def set_image():
    global image
    image = ImageGrab.grab()

def image_set():
    return image != 0

def get_color(p):
    if p[0] < 0: p = (0, p[1])
    if p[1] < 0: p = (p[0], 0)
    get_image()
    # print p
    color = image.getpixel(p)
    color_str = str(color[0]) + str(color[1]) + str(color[2])
    return int(color_str)

# get_image()
#
# for x in range(10,600,50):
#     for y in range (300, 900, 50):
#         t = get_color((x,y))
#         print t[0] == 0 and t[1] == 0 and t[2] == 0

# i = ImageGrab.grab()
# print i.size
# print i.getpixel((i.size[0]-1,i.size[1]-1))

# i = ImageGrab.grab()
# print i.getpixel((300,300)) == (0,0,0)
