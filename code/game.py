#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.controls import Controls
from code.level import Level


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        menu = Menu(self.window)

        while True:

            option = menu.run()

            if option == "NEW GAME":

                level = Level(self.window)
                level.run()

            elif option == "CONTROLS":

                controls = Controls(self.window)
                controls.run()

            elif option == "EXIT":

                pygame.quit()
                quit()
