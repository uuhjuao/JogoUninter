#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

# os inimigos e jogadores serão gerados daqui
class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = None
        self.surf = None

    def move(self, ):
        pass
