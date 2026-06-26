#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.entity import Entity
from code.const import WIN_WIDTH, GROUND_Y


class Enemy(Entity):

    def __init__(self, side):

        if side == "LEFT":
            x = -50
            self.direction = "RIGHT"
        else:
            x = WIN_WIDTH + 50
            self.direction = "LEFT"

        super().__init__(
            "Enemy",
            "./asset/enemy.png",
            x,
            GROUND_Y
        )

        # Ajusta o tamanho do inimigo
        self.surf = pygame.transform.scale(self.surf, (50, 70))

        # Atualiza o rect após redimensionar
        self.rect = self.surf.get_rect(midbottom=(x, GROUND_Y))

        self.speed = 2

    def update(self, player):
        self.move(player)

    def move(self, player):

        if self.rect.centerx < player.rect.centerx:
            self.rect.x += self.speed
            self.direction = "RIGHT"

        elif self.rect.centerx > player.rect.centerx:
            self.rect.x -= self.speed
            self.direction = "LEFT"

    def draw(self, window):

        if self.direction == "LEFT":
            image = pygame.transform.flip(self.surf, True, False)
            window.blit(image, self.rect)
        else:
            window.blit(self.surf, self.rect)