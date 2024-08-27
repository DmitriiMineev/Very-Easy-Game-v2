from tkinter import Tk, Label

from settings import settings_command
from settings import exit_command

from game import start_game_command

from other import std_button

from constants import STD_WINDOW_WIDTH, STD_WINDOW_HEIGHT, STD_FONT_SIZE, STD_INDENT_Y


def make_start_window():
    """
    Создает стартовое окно игры `root`, метку `game_name`
    и кнопки
    `start_button`, `settings_button`, `exit_button`,
    конструирует их и размещает всё это добро внутри окна.

    Кнопке `start_button` назначается команда
    `start_game_command`
    из game.py, кнопке `settings_button` команда
    `settings_command`
    из settings.py, кнопке `exit_button`
    запуск диалогового окна с
    уточнением, хочет ли пользователь выйти из игры.
    """
    root = Tk()
    root['bg'] = 'black'
    root.title("Very Easy Game")
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    width = width // 2
    height = height // 2
    width = width - STD_WINDOW_WIDTH // 2
    height = height - STD_WINDOW_HEIGHT // 2
    root.geometry('{}x{}+{}+{}'.format(STD_WINDOW_WIDTH, STD_WINDOW_HEIGHT, width, height))

    game_name = Label()
    game_name.config(text="Very Easy Game")
    game_name.config(bg="black")
    game_name.config(foreground="white")
    game_name.config(font='TkDefaultFont {}'.format(STD_FONT_SIZE))

    start_but = std_button(root)
    start_but.config(text="Start")
    start_but.config(command=start_game_command)

    settings_but = std_button(root)
    settings_but.config(text="Settings")
    settings_but.config(command=settings_command)

    exit_but = std_button(root)
    exit_but.config(text="Exit")
    exit_but.config(command=exit_command)

    game_name.pack(pady=2 * STD_INDENT_Y)
    start_but.pack(pady=STD_INDENT_Y)
    settings_but.pack(pady=STD_INDENT_Y)
    exit_but.pack(pady=STD_INDENT_Y)

    root.mainloop()
