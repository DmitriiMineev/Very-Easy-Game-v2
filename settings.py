import sys
from tkinter import messagebox as mb, Label, Toplevel

from constants import MIDDLE_MIN_INDENT, MIDDLE_MAX_INDENT, MIDDLE_HOLE_WIDTH, MIDDLE_PLAYER_SHIFT, STD_WINDOW_WIDTH, \
    STD_WINDOW_HEIGHT, STD_FONT_SIZE, EASY_MIN_INDENT, EASY_HOLE_WIDTH, EASY_MAX_INDENT, EASY_PLAYER_SHIFT, \
    HARD_MIN_INDENT, HARD_MAX_INDENT, HARD_PLAYER_SHIFT, HARD_HOLE_WIDTH, STD_INDENT_Y
from other import std_button

min_indent = MIDDLE_MIN_INDENT
max_indent = MIDDLE_MAX_INDENT
hole_width = MIDDLE_HOLE_WIDTH
player_shift = MIDDLE_PLAYER_SHIFT


def change_level(l_min_indent, l_max_indent, l_hole_width, l_player_shift):
    """
    Изменяет параметры уровня сложности `min_indent`,
    `max_indent`, `hole_width`, `player_shift` в передаваемые
    значения `l_min_indent`, `l_max_indent`, `l_hole_width`,
    `l_player_shift` соответственно.
    :param l_min_indent: Минимальный отступ между препятствиями.
    :param l_max_indent: Максимальный отступ между препятствиями.
    :param l_hole_width: Ширина промежутка в препятствии, через который нужно проезжать игроку.
    :param l_player_shift: Переменная, отвечающая за то, насколько быстро игрок будет двигаться
    """
    global min_indent
    global max_indent
    global hole_width
    global player_shift
    min_indent = l_min_indent
    max_indent = l_max_indent
    hole_width = l_hole_width
    player_shift = l_player_shift


def exit_command():
    """
    Создает диалоговое окно, уточняющее, действительно ли
    пользователь хочет выйти из игры, в случае утвердительного
    ответа закрывает игру.
    """
    answer = mb.askyesno(
        title="Exit",
        message="Do you really want to exit?")
    if answer:
        sys.exit()


def settings_command():
    """
    Создает окно настроек, метку `section_name`
    и кнопки `easy_button`, `middle_button`,
    `hard_button` и `back_button`, конструирует их и
    размещает всё это добро внутри окна.

    Каждая из кнопок выбора сложности вызывает `change_level`
    с соответствующими параметрами уровня сложности.

    Кнопке `back_button` назначается команда
    `setting_window.destroy`
    """
    setting_window = Toplevel()
    setting_window['bg'] = 'black'
    setting_window.title("Settings")
    width = setting_window.winfo_screenwidth()
    height = setting_window.winfo_screenheight()
    width = width // 2
    height = height // 2
    width = width - STD_WINDOW_WIDTH // 2
    height = height - STD_WINDOW_WIDTH // 2
    setting_window.geometry('{}x{}+{}+{}'.format(STD_WINDOW_WIDTH, STD_WINDOW_HEIGHT, width, height))

    section_name = Label(setting_window)
    section_name.config(text="Please choose\nthe difficulty level")
    section_name.config(bg="black")
    section_name.config(foreground="white")
    section_name.config(font='TkDefaultFont {}'.format(STD_FONT_SIZE))

    easy_but = std_button(setting_window)
    easy_but.config(text="Easy")
    easy_but.config(command=lambda: change_level(EASY_MIN_INDENT, EASY_MAX_INDENT,
                                                 EASY_HOLE_WIDTH, EASY_PLAYER_SHIFT))

    middle_but = std_button(setting_window)
    middle_but.config(text="Middle")
    middle_but.config(command=lambda: change_level(MIDDLE_MIN_INDENT, MIDDLE_MAX_INDENT,
                                                   MIDDLE_HOLE_WIDTH, MIDDLE_PLAYER_SHIFT))

    hard_but = std_button(setting_window)
    hard_but.config(text="Hard")
    hard_but.config(command=lambda: change_level(HARD_MIN_INDENT, HARD_MAX_INDENT,
                                                 HARD_HOLE_WIDTH, HARD_PLAYER_SHIFT))

    back_but = std_button(setting_window)
    back_but.config(text="Back")
    back_but.config(command=lambda: setting_window.destroy())

    section_name.pack(pady=2 * STD_INDENT_Y)
    easy_but.pack(pady=STD_INDENT_Y)
    middle_but.pack(pady=STD_INDENT_Y)
    hard_but.pack(pady=STD_INDENT_Y)
    back_but.pack(pady=STD_INDENT_Y)

    setting_window.mainloop()
