#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.const import WIN_WIDTH, COLOR_WHITE
from code.player import Player
from code.HUD import HUD
from code.enemy import Enemy


class Level:

    def __init__(self, window):

        self.window = window

        # Fundo da fase
        self.surf = pygame.image.load("./asset/back3.png")
        self.rect = self.surf.get_rect(left=0, top=0)

        # Jogador
        self.player = Player()

        #HUD
        self.hud = HUD()

        # Dados da partida
        self.time = 60

        # Enemies
        self.enemy_list = []

        self.enemy_list.append(
            Enemy("LEFT")
        )

    def run(self):

        clock = pygame.time.Clock()

        while True:

            clock.tick(60)

            # Captura as teclas pressionadas
            keys = pygame.key.get_pressed()

            # Move o jogador
            self.player.move(keys)

            # Desenha o fundo
            self.window.blit(self.surf, self.rect)

            # Desenha o jogador
            self.player.draw(self.window)

            for enemy in self.enemy_list:
                enemy.draw(self.window)


            self.hud.draw(
                self.window,
                self.player,
                self.time
            )

            self.player.update()

            for enemy in self.enemy_list:
                enemy.update(self.player)

            pygame.display.flip()

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:
                        self.player.attack()

                    if event.key == pygame.K_ESCAPE:
                        return

    def draw_hearts(self):

        start_x = WIN_WIDTH - 90
        start_y = 10

        for i in range(self.player.life):
            self.window.blit(
                self.heart,
                (start_x + i * 28, start_y)
            )