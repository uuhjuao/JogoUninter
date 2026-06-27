#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.const import WIN_WIDTH, COLOR_GREEN, COLOR_WHITE


class GameOver:

    def __init__(self, window, result, player_name, time_survived, kills):

        self.player_name = player_name
        self.time_survived = time_survived
        self.kills = kills

        self.window = window
        self.result = result

        self.surf = pygame.image.load("./asset/back3.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):

        while True:

            # Fundo
            self.window.blit(self.surf, self.rect)

            # Mensagem principal
            if self.result == "WIN":
                title = "YOU WIN!"
            else:
                title = "YOU LOSE!"

                self.draw_text(
                    22,
                    f"Player: {self.player_name}",
                    COLOR_WHITE,
                    (WIN_WIDTH / 2, 140)
                )

                self.draw_text(
                    22,
                    f"Time Survived: {self.time_survived}s",
                    COLOR_WHITE,
                    (WIN_WIDTH / 2, 180)
                )

                self.draw_text(
                    22,
                    f"Enemies Defeated: {self.kills}",
                    COLOR_WHITE,
                    (WIN_WIDTH / 2, 220)
                )

            self.draw_text(
                40,
                title,
                COLOR_GREEN,
                (WIN_WIDTH / 2, 300)
            )

            # Mensagem secundária
            if self.result == "WIN":
                message = "You survived for 60 seconds!"
            else:
                message = "You were defeated!"

            self.draw_text(
                22,
                message,
                COLOR_WHITE,
                (WIN_WIDTH / 2, 140)
            )

            self.draw_text(
                20,
                "Press ENTER to return to Menu",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 80)
            )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RETURN:
                        return

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