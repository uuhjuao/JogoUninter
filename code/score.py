#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import pygame

from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_WIDTH, COLOR_GREEN, COLOR_WHITE


class Score:

    def __init__(self, window):

        self.window = window

        self.surf = pygame.image.load("./asset/back3.png")
        self.rect = self.surf.get_rect(left=0, top=0)

        self.scores = self.load_scores()

    def load_scores(self):

        try:

            with open("score.json", "r") as file:
                return json.load(file)

        except:

            return []

    def run(self):

        while True:

            self.window.blit(self.surf, self.rect)

            self.draw_text(
                40,
                "SCORE",
                COLOR_GREEN,
                (WIN_WIDTH / 2, 50)
            )

            # Cabeçalho
            self.draw_text(
                22,
                "PLAYER        TIME      KILLS",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 100)
            )

            # Lista de pontuações
            y = 140

            for score in self.scores:

                line = f"{score['name']:<12} {score['time']:<8} {score['kills']}"

                self.draw_text(
                    20,
                    line,
                    COLOR_WHITE,
                    (WIN_WIDTH / 2, y)
                )

                y += 30

            self.draw_text(
                20,
                "Press ESC to return",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 340)
            )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
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