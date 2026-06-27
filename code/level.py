#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.const import WIN_WIDTH, COLOR_WHITE, MAX_ENEMIES
from code.player import Player
from code.HUD import HUD
from code.enemy import Enemy
import random



class Level:

    def __init__(self, window, player_name):

        self.window = window
        self.player_name = player_name

        # Fundo da fase
        self.surf = pygame.image.load("./asset/back3.png")
        self.rect = self.surf.get_rect(left=0, top=0)

        # Jogador
        self.player = Player()

        #HUD
        self.hud = HUD()

        # Informações do jogo
        self.time = 60
        self.kills = 0
        self.start_time = pygame.time.get_ticks()

        # Enemies
        self.enemy_list = []
        self.spawn_time = pygame.time.get_ticks()


    def run(self):

        clock = pygame.time.Clock()


        while True:

            clock.tick(60)

            current_time = pygame.time.get_ticks()
            self.time = 60 - (current_time - self.start_time) // 1000

            elapsed = (pygame.time.get_ticks() - self.start_time) // 1000
            self.time = max(0, 60 - elapsed)
            if self.time <= 0:
                return "WIN"

            self.spawn_enemy()

            keys = pygame.key.get_pressed()

            # Atualiza
            self.player.move(keys)

            self.player.update()
            if self.player.life <= 0:
                return "LOSE"

            self.check_attack_collision()

            for enemy in self.enemy_list:
                enemy.update(self.player)

                # Verifica derrota
                if self.player.life <= 0:
                    return (
                        "LOSE",
                        self.player_name,
                        60 - self.time,
                        self.kills
                    )

                # Verifica vitória
                if self.time <= 0:
                    return (
                        "WIN",
                        self.player_name,
                        60 - self.time,
                        self.kills
                    )

                self.enemy_list = [
                    enemy
                    for enemy in self.enemy_list
                    if enemy.alive
                ]

            # Desenha
            self.window.blit(self.surf, self.rect)

            self.player.draw(self.window)

            for enemy in self.enemy_list:
                enemy.draw(self.window)

            self.hud.draw(
                self.window,
                self.player,
                self.player_name,
                self.time,
                self.kills
            )

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

    def check_attack_collision(self):

        if not self.player.attacking:
            return

        for enemy in self.enemy_list:

            if not enemy.alive:
                continue

            attack_rect = self.player.rect.copy()

            if self.player.direction == "RIGHT":
                attack_rect.width += 30

            else:
                attack_rect.x -= 30
                attack_rect.width += 30

            if attack_rect.colliderect(enemy.rect):
                self.kills += 1
                enemy.die()

    def spawn_enemy(self):

        current_time = pygame.time.get_ticks()

        if (
                current_time - self.spawn_time >= 3000
                and len(self.enemy_list) < MAX_ENEMIES
        ):
            side = random.choice(["LEFT", "RIGHT"])

            self.enemy_list.append(
                Enemy(side)
            )

            self.spawn_time = current_time