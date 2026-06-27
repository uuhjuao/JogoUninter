#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_WIDTH, COLOR_GREEN, COLOR_WHITE


class NameInput:

    def __init__(self, window):

        self.window = window

        self.surf = pygame.image.load("./asset/back3.png")
        self.rect = self.surf.get_rect(left=0, top=0)

        self.player_name = ""

    def run(self):

        while True:

            self.window.blit(self.surf, self.rect)

            self.draw_text(
                40,
                "ENTER YOUR NAME",
                COLOR_GREEN,
                (WIN_WIDTH / 2, 70)
            )

            self.draw_text(
                30,
                self.player_name + "_",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 150)
            )

            self.draw_text(
                20,
                "Press ENTER to start",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 250)
            )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    # ENTER
                    if event.key == pygame.K_RETURN:

                        if len(self.player_name) > 0:
                            return self.player_name

                    # BACKSPACE
                    elif event.key == pygame.K_BACKSPACE:

                        self.player_name = self.player_name[:-1]

                    else:

                        # Aceita somente letras e números
                        if event.unicode.isalnum():

                            if len(self.player_name) < 12:

                                self.player_name += event.unicode.upper()

    def draw_text(self, size, text, color, center):

        font: Font = pygame.font.SysFont(
            "Lucida Sans Typewriter",
            size
        )

        surface: Surface = font.render(
            text,
            True,
            color
        ).convert_alpha()

        rect: Rect = surface.get_rect(center=center)

        self.window.blit(surface, rect)