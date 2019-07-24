import pyperclip


def grab_clipboard():
    return pyperclip.paste()


def set_clipboard_text(some_text):
    pyperclip.copy(some_text)


def paste():
    pyperclip.paste()
