#!/usr/bin/python
# -*- coding: utf-8 -*-

import json
import pygame
from pathlib import Path

from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_WIDTH, COLOR_GREEN, COLOR_WHITE


class Score:

    def __init__(self, window):
        self.window = window

        self.surf = pygame.image.load("./asset/back3.png")
        self.rect = self.surf.get_rect(left=0, top=0)

        self.score_file = Path("score.json")
        self.scores = []
        self.scroll = 0

    def load_scores(self):
        try:
            with open(self.score_file, "r") as file:
                return json.load(file)
        except:
            return []

    def save_score(self, name, time, kills):
        scores = self.load_scores()

        scores.append({
            "name": name,
            "time": time,
            "kills": kills
        })

        with open(self.score_file, "w") as file:
            json.dump(scores, file, indent=4)

    def run(self):
        self.scores = self.load_scores()

        while True:
            self.window.blit(self.surf, self.rect)

            self.draw_text(
                40,
                "SCORE",
                COLOR_GREEN,
                (WIN_WIDTH / 2, 40)
            )

            self.draw_text(
                20,
                "PLAYER        TIME      KILLS",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 85)
            )

            y = 120
            visible_scores = self.scores[self.scroll:self.scroll + 5]

            for score in visible_scores:
                line = f"{score['name']:<12} {score['time']:<8} {score['kills']}"

                self.draw_text(
                    18,
                    line,
                    COLOR_WHITE,
                    (WIN_WIDTH / 2, y)
                )

                y += 30

            self.draw_text(
                18,
                "UP/DOWN - Scroll",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 285)
            )

            self.draw_text(
                18,
                "ESC - Return",
                COLOR_WHITE,
                (WIN_WIDTH / 2, 310)
            )

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        return

                    elif event.key == pygame.K_DOWN:
                        if self.scroll < len(self.scores) - 5:
                            self.scroll += 1

                    elif event.key == pygame.K_UP:
                        if self.scroll > 0:
                            self.scroll -= 1

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