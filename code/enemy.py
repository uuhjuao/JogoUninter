#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.entity import Entity
from code.const import GROUND_Y, ENEMY_GROUND_OFFSET, WIN_WIDTH


class Enemy(Entity):

    def __init__(self, side):

        self.attack_time = None
        self.attacking = None
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

        # Idle
        self.idle_image = pygame.image.load("./asset/enemy.png").convert_alpha()
        self.idle_image = pygame.transform.scale(self.idle_image, (50, 70))

        # Attack
        self.attack_image = pygame.image.load("./asset/enemy_attack.png").convert_alpha()
        self.attack_image = pygame.transform.scale(self.attack_image, (50, 70))

        # Versões espelhadas
        self.idle_left = pygame.transform.flip(self.idle_image, True, False)
        self.attack_left = pygame.transform.flip(self.attack_image, True, False)

        # Imagem atual
        if self.direction == "RIGHT":
            self.surf = self.idle_image
        else:
            self.surf = self.idle_left

        self.alive = True

        # Ajusta o tamanho do inimigo
        self.surf = pygame.transform.scale(self.surf, (50, 70))

        # Atualiza o rect após redimensionar
        self.rect = self.surf.get_rect(
            midbottom=(x, GROUND_Y + ENEMY_GROUND_OFFSET)
        )

        self.speed = 2

        # Controle do ataque
        self.attack_delay = 1000  # 1 segundo
        self.last_attack = pygame.time.get_ticks()

    def update(self, player):

        if not self.alive:
            return

        self.move(player)

        self.attack(player)

        self.animation()

        # Futuramente:
        # self.attack(player)

    def move(self, player):

        distance = abs(self.rect.centerx - player.rect.centerx)

        if distance > 55:

            if self.rect.centerx < player.rect.centerx:

                self.rect.x += self.speed
                self.direction = "RIGHT"

            else:

                self.rect.x -= self.speed
                self.direction = "LEFT"

    def attack(self, player):

        distance = abs(self.rect.centerx - player.rect.centerx)

        if distance <= 55:

            current_time = pygame.time.get_ticks()

            if current_time - self.last_attack >= self.attack_delay:

                self.attacking = True
                self.attack_time = current_time

                if self.direction == "RIGHT":
                    self.surf = self.attack_image
                else:
                    self.surf = self.attack_left

                player.life -= 1

                self.last_attack = current_time

    def animation(self):

        if self.attacking:

            current_time = pygame.time.get_ticks()

            if current_time - self.attack_time > 200:

                self.attacking = False

                if self.direction == "RIGHT":
                    self.surf = self.idle_image
                else:
                    self.surf = self.idle_left

    def draw(self, window):
        window.blit(self.surf, self.rect)

    def die(self):
        self.alive = False
