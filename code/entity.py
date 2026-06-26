#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

import pygame


# os inimigos e jogadores serão gerados daqui
class Entity(ABC): # uma classe abstrata implica quw todos os metodos serão implementados pelos seus fihos
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./asset/backgame.png')
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod # isso aqui é um decorator
    def move(self, ):

