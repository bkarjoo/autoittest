from PIL import ImageGrab

image = None

def set_image():
    global image
    image = ImageGrab.grab()

def get_color(p):
    if image is None:
        print "Image not grabbed yet."
        return None
    try:
        p = (p[0]-1,p[1]-1)
        return image.getpixel(p)
    except:
        return (-1,-1,-1)
