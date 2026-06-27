#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_WIDTH, COLOR_GREEN, COLOR_WHITE


class GameOver:

    def __init__(self, window, result, player_name, time_survived, kills):

        self.window = window
        self.result = result

        self.player_name = player_name
        self.time_survived = time_survived
        self.kills = kills

        self.surf = pygame.image.load("./asset/back3.png")
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):

        while True:

            # Fundo
            self.window.blit(self.surf, self.rect)

            # Define título e mensagem
            if self.result == "WIN":
                title = "YOU WIN!"
                message = "You survived!"
            else:
                title = "YOU LOSE!"
                message = "You were defeated!"

            # Título
            self.draw_text(
                40,
                title,
                COLOR_GREEN,
                (WIN_WIDTH / 2, 70)
            )

            # Mensagem
            self.draw_text(
                22,
                message,
                COLOR_WHITE,
                (WIN_WIDTH / 2, 120)
            )

            # Nome do jogador
            self.draw_text(
                22,
                f"Player: {self.player_name}",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 170)
            )

            # Tempo sobrevivido
            self.draw_text(
                22,
                f"Time Survived: {self.time_survived}s",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 205)
            )

            # Inimigos derrotados
            self.draw_text(
                22,
                f"Enemies Defeated: {self.kills}",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 240)
            )

            # Instrução
            self.draw_text(
                20,
                "Press ENTER to return to Menu",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 310)
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