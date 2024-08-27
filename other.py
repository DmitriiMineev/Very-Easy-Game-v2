from tkinter import Button

from constants import STD_BUTTON_WIDTH, STD_FONT_SIZE


def std_button(parent):
    ret = Button(parent)
    ret.config(width=STD_BUTTON_WIDTH)
    ret.config(bg="white")
    ret.config(foreground="black")
    ret.config(font='TkDefaultFont {}'.format(STD_FONT_SIZE))
    return ret
