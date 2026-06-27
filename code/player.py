#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.entity import Entity
from code.const import WIN_WIDTH, GROUND_Y


class Player(Entity):


    def __init__(self):

        super().__init__(
            "Player",
            "./asset/player_idle.png",
            WIN_WIDTH // 2,
            GROUND_Y
        )

        self.speed = 5

        self.life = 3

        self.direction = "RIGHT"

        # Idle
        self.idle_image = pygame.image.load("./asset/player_idle.png").convert_alpha()
        self.idle_image = pygame.transform.scale(self.idle_image, (60, 80))

        # Ataque
        self.attack_image = pygame.image.load("./asset/player_attack.png").convert_alpha()
        self.attack_image = pygame.transform.scale(self.attack_image, (60, 80))

        # Versões para esquerda
        self.idle_left = pygame.transform.flip(self.idle_image, True, False)
        self.attack_left = pygame.transform.flip(self.attack_image, True, False)

        # Imagem atual
        self.surf = self.idle_image

        # Controle do ataque
        self.attacking = False
        self.attack_time = 0

        self.attacking = False

        self.attack_time = 0

    def move(self, keys):

        # Movimento para a esquerda
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
            self.direction = "LEFT"

            if not self.attacking:
                self.surf = self.idle_left

        # Movimento para a direita
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
            self.direction = "RIGHT"

            if not self.attacking:
                self.surf = self.idle_image


        # Limite esquerdo
        if self.rect.left < 0:
            self.rect.left = 0

        # Limite direito
        if self.rect.right > WIN_WIDTH:
            self.rect.right = WIN_WIDTH

    def attack(self):

        if not self.attacking:
            self.attacking = True

            self.attack_time = pygame.time.get_ticks()

            if self.direction == "RIGHT":
                self.surf = self.attack_image
            else:
                self.surf = self.attack_left

    def update(self):

        if self.attacking:

            current_time = pygame.time.get_ticks()

            if current_time - self.attack_time > 200:
                self.attacking = False

                if self.direction == "RIGHT":
                    self.surf = self.idle_image
                else:
                    self.surf = self.idle_left