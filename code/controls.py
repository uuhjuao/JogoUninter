#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.const import WIN_WIDTH, WIN_HEIGHT, COLOR_WHITE, COLOR_GREEN


class Controls:

    def __init__(self, window):
        self.rect = None
        self.surf = None
        self.window = window
        self.surf = pygame.image.load('./asset/back3.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):

        while True:

            self.window.blit(self.surf, self.rect)

            self.draw_text(40, "CONTROLS", COLOR_GREEN, (WIN_WIDTH / 2, 40))

            self.draw_text(22, "A ou <- : Mover para esquerda", COLOR_WHITE, (WIN_WIDTH / 2, 100))

            self.draw_text(22, "D ou -> : Mover para direita", COLOR_WHITE, (WIN_WIDTH / 2, 140))

            self.draw_text(22, "SPACE : Atacar", COLOR_WHITE, (WIN_WIDTH / 2, 180))

            self.draw_text(22, "ESC : Voltar ao menu", COLOR_WHITE, (WIN_WIDTH / 2, 260))

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_ESCAPE:
                        return

    def draw_text(self, size, text, color, center):

        font: Font = pygame.font.SysFont("Lucida Sans Typewriter", size)

        surface: Surface = font.render(text, True, color).convert_alpha()

        rect: Rect = surface.get_rect(center=center)

        self.window.blit(surface, rect)