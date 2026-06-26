#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame


class Entity:

    def __init__(self, name, image_path, x, y):

        self.name = name

        self.surf = pygame.image.load(image_path).convert_alpha()

        self.surf = pygame.transform.scale(
            self.surf,
            (35, 40)
        )

        self.rect = self.surf.get_rect(midbottom=(x, y))

    def draw(self, window):

        window.blit(self.surf, self.rect)

