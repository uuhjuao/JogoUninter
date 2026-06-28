#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
import random

from code.const import WIN_WIDTH, MAX_ENEMIES
from code.player import Player
from code.HUD import HUD
from code.enemy import Enemy


class Level:

    def __init__(self, window, player_name):

        self.window = window
        self.player_name = player_name

        # Fundo da fase
        self.surf = pygame.image.load("./asset/back3.png")
        self.rect = self.surf.get_rect(left=0, top=0)

        # Jogador
        self.player = Player()

        # HUD
        self.hud = HUD()

        # Informações do jogo
        self.time = 60
        self.kills = 0
        self.start_time = pygame.time.get_ticks()

        # Inimigos
        self.enemy_list = []
        self.spawn_time = pygame.time.get_ticks()

    def run(self):

        clock = pygame.time.Clock()

        pygame.mixer_music.load("./asset/attack_on_titan.mp3")
        pygame.mixer_music.play(-1)

        while True:

            clock.tick(60)

            # Atualiza tempo
            elapsed = (pygame.time.get_ticks() - self.start_time) // 1000
            self.time = max(0, 60 - elapsed)

            # Verifica vitória
            if self.time <= 0:
                return (
                    "WIN",
                    self.player_name,
                    60,
                    self.kills
                )

            # Cria inimigos
            self.spawn_enemy()

            # Captura teclas
            keys = pygame.key.get_pressed()

            # Atualiza jogador
            self.player.move(keys)
            self.player.update()

            # Verifica derrota
            if self.player.life <= 0:
                return (
                    "LOSE",
                    self.player_name,
                    60 - self.time,
                    self.kills
                )

            # Verifica ataque do jogador nos inimigos
            self.check_attack_collision()

            # Atualiza inimigos
            for enemy in self.enemy_list:
                enemy.update(self.player)

            # Remove inimigos mortos
            self.enemy_list = [
                enemy
                for enemy in self.enemy_list
                if enemy.alive
            ]

            # Verifica derrota novamente após ataque dos inimigos
            if self.player.life <= 0:
                return (
                    "LOSE",
                    self.player_name,
                    60 - self.time,
                    self.kills
                )

            # Desenha fundo
            self.window.blit(self.surf, self.rect)

            # Desenha jogador
            self.player.draw(self.window)

            # Desenha inimigos
            for enemy in self.enemy_list:
                enemy.draw(self.window)

            # Desenha HUD
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
                        return (
                            "LOSE",
                            self.player_name,
                            60 - self.time,
                            self.kills
                        )

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