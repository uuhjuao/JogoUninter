#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from pygame.font import Font
from pygame.surface import Surface
from pygame.rect import Rect

from code.const import WIN_WIDTH, COLOR_WHITE


class HUD:

    def __init__(self):

        # Carrega o coração
        self.heart = pygame.image.load("./asset/heart.png").convert_alpha()
        self.heart = pygame.transform.scale(self.heart, (24, 24))

    def draw(self, window, player, player_name, time, kills):
        # Nome do jogador
        self.draw_text(
            window,
            20,
            f"Player: {player_name}",
            COLOR_WHITE,
            (90, 20)
        )

        # Tempo
        self.draw_text(
            window,
            20,
            f"Tempo: {time}",
            COLOR_WHITE,
            (90, 50)
        )

        # Kills
        self.draw_text(
            window,
            20,
            f"Kills: {kills}",
            COLOR_WHITE,
            (90, 80)
        )

        # Corações
        self.draw_hearts(window, player.life)

    def draw_hearts(self, window, life):

        start_x = WIN_WIDTH - 100

        for i in range(life):

            window.blit(
                self.heart,
                (start_x + i * 28, 8)
            )

    def draw_text(self, window, size, text, color, center):

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

        window.blit(surface, rect)