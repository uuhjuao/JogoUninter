#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT
from code.controls import Controls
from code.level import Level
from code.gameover import GameOver
from code.nameinput import NameInput


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        menu = Menu(self.window)

        while True:

            option = menu.run()

            if option == "NEW GAME":

                # Tela para digitar o nome
                name_input = NameInput(self.window)

                player_name = name_input.run()

                # Inicia a fase
                level = Level(
                    self.window,
                    player_name
                )
                result, player_name, time_survived, kills = level.run()

                game_over = GameOver(
                    self.window,
                    result,
                    player_name,
                    time_survived,
                    kills
                )

                game_over.run()

                if result == "WIN":
                    print("YOU WIN")

                elif result == "LOSE":
                    print("YOU LOSE")

            elif option == "CONTROLS":

                controls = Controls(self.window)
                controls.run()

            elif option == "EXIT":

                pygame.quit()
                quit()
