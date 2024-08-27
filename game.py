from tkinter import Toplevel, Label

import pygame as pg
import sys
import random

from constants import STD_FONT_SIZE, STD_BARRIER_HEIGHT, STD_SHIFT, STD_PLAYER_HEIGHT, STD_PLAYER_WIDTH, \
    STD_WINDOW_WIDTH, STD_WINDOW_HEIGHT, BIG_FONT_SIZE, SCORE_COUNT_SPEED, STD_FPS

pg.font.init()
font_score = pg.font.Font(None, STD_FONT_SIZE)


def start_game_command():
    """
    Функция игры.

    Создает окно (поверхность) игры `sc`. Заводит счётчик
    `score_count` очков игрока и текст `score text`
    под него на окне.

    Создаёт левую и правую группы препятствий
    `barriers_left` и `barriers_right` из объектов
    класса `Barrier`. Создает игрока `player` - объект класса
    `Player`.

    Заводится переменная `highest` для отслеживания самого
    высокого препятствия, а также флаги `is_left` и `is_right`,
    в которых хранится информация о том, нажаты ли левая и
    правая стрелки соответственно.

    Запускается основной цикл игры.

    Проверяется, какие клавиши нажаты, в соответствии с этим
    обновляются значения `is_left` и `is_right`.
    В соответствии с этим дальше двигается игрок.
    Обновляется `sc`.

    Далее проверяется, не пересекается ли игрок с барьерами.
    Если пересекается, то создается окно `lose_window` и
    текстовые метки на нём, сообщающие о поражении и
    о набранных очках.

    Проверяется значение highest. В случае необходимости
    создаются новые `Barrier` и добавляются в `barriers_left`
    и `barriers_right`.

    Объекты `barriers_left` и `barriers_right` прикрепляются
    к `sc`, после чего модифицируются.

    Обновляются `highest`, `score_count`, `score_text`,
    прикрепляется к `sc`, после чего экран обновляется.
    """
    from settings import hole_width
    from settings import min_indent
    from settings import max_indent
    from settings import player_shift

    class Barrier(pg.sprite.Sprite):
        """
        Класс препятствий, наследник `Sprite`.

        Имеет `width`, `height`, `color`, родительскую поверхность
        `parent`. Имеет конструктор, собирающий `Barrier` из всего
        этого.

        Имеет метод `update`, сдвигающий препятствие вниз.
        """
        def __init__(self, surface, x_beg, width, y_beg, color, height=STD_BARRIER_HEIGHT):
            pg.sprite.Sprite.__init__(self)
            self.height = height
            self.width = width
            self.parent = surface
            self.color = color
            self.image = pg.Surface((self.width, self.height))
            self.image.fill(self.color)
            self.rect = self.image.get_rect(topleft=(x_beg, y_beg - self.height))

        def update(self):
            """
            Сдвигает 'Barrier' вниз.
            """
            self.rect.y += STD_SHIFT
            if self.rect.y > self.parent.get_height():
                self.kill()

    class Player(pg.sprite.Sprite):
        """
        Класс игрока, наследник `Sprite`.

        Имеет `width`, `height`, `color`, родительскую поверхность
        `parent`. Имеет конструктор, собирающий `Player` из всего
        этого.

        Имеет метод `update_left`, сдвигающий игрока влево.
        Имеет метод `update_right`, сдвигающий игрока вправо.
        """
        def __init__(self, surface, color):
            pg.sprite.Sprite.__init__(self)
            self.height = STD_PLAYER_HEIGHT
            self.width = STD_PLAYER_WIDTH
            self.parent = surface
            self.color = color
            self.image = pg.Surface((self.width, self.height))
            self.image.fill(self.color)
            self.rect = self.image.get_rect(center=(self.parent.get_width() // 2,
                                                    self.parent.get_height() - self.height // 2))

        def update_left(self):
            """
            Сдвигает игрока влево.
            """
            self.rect.x -= player_shift
            # if 2 * (self.rect.x - player_shift) >= self.width:
            #     self.rect.x -= player_shift
            # else:
            #     self.rect.x = self.width / 2 - 10

        def update_right(self):
            self.rect.x += player_shift
            """
            Сдвигает игрока вправо.
            """
            # if 2 * (self.rect.x + player_shift) + self.width <= 2 * self.parent.get_width():
            #     self.rect.x += player_shift
            # else:
            #     self.rect.x = self.parent.get_width() - ((self.width - 1) / 2)

    clock = pg.time.Clock()

    sc = pg.display.set_mode((STD_WINDOW_WIDTH, STD_WINDOW_HEIGHT))
    sc.fill('black')
    pg.display.update()

    score_count = 0.0

    score_text = font_score.render('Your score: {}'.format(int(score_count)), False, 'green', 'black')
    sc.blit(score_text, (0, 0))

    barriers_left = pg.sprite.Group()
    barriers_right = pg.sprite.Group()

    player = Player(sc, 'red')

    highest = 0

    is_left = False
    is_right = False

    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                sys.exit()
            elif i.type == pg.KEYDOWN:
                if i.key == pg.K_LEFT:
                    is_left = True
                    is_right = False
                elif i.key == pg.K_RIGHT:
                    is_right = True
                    is_left = False
            elif i.type == pg.KEYUP:
                is_left = False
                is_right = False

        if is_left:
            player.update_left()
        elif is_right:
            player.update_right()

        sc.fill('black')
        sc.blit(player.image, player.rect)

        if pg.sprite.spritecollideany(player, barriers_left) or pg.sprite.spritecollideany(player, barriers_right):
            lose_window = Toplevel()
            lose_window['bg'] = 'black'
            lose_window.title("Very Easy Game")
            width = lose_window.winfo_screenwidth()
            height = lose_window.winfo_screenheight()
            width = width // 2
            height = height // 2
            width = width - STD_WINDOW_WIDTH // 2
            height = height - STD_WINDOW_HEIGHT // 2
            lose_window.geometry('{}x{}+{}+{}'.format(STD_WINDOW_WIDTH, STD_WINDOW_HEIGHT, width, height))

            lose_label = Label(lose_window)
            lose_label.config(text="You lose\nYour score: {}".format(int(score_count)))
            lose_label.config(bg="black")
            lose_label.config(foreground="blue")
            lose_label.config(font='TkDefaultFont {}'.format(BIG_FONT_SIZE))

            lose_label.pack(pady=STD_WINDOW_HEIGHT // 4)

            lose_window.mainloop()
            pg.quit()
            exit()

        if -2 <= highest <= 0:
            x_end = random.randint(0, sc.get_width() - hole_width)
            new_bar_left = Barrier(sc,
                                   0,
                                   x_end,
                                   highest - STD_BARRIER_HEIGHT,
                                   'white')
            new_bar_right = Barrier(sc,
                                    x_end + hole_width,
                                    sc.get_width() - x_end + hole_width,
                                    highest - STD_BARRIER_HEIGHT,
                                    'white')

            indent_height = STD_BARRIER_HEIGHT * random.randint(min_indent, max_indent)
            highest = highest - new_bar_left.height - indent_height

            barriers_left.add(new_bar_left)
            barriers_right.add(new_bar_right)

        barriers_left.draw(sc)
        barriers_right.draw(sc)

        barriers_left.update()
        barriers_right.update()

        highest += STD_SHIFT

        score_count += SCORE_COUNT_SPEED
        score_text = font_score.render('Your score: {}'.format(int(score_count)), True, 'green', 'black')
        sc.blit(score_text, (0, 0))

        pg.display.update()

        clock.tick(STD_FPS)
