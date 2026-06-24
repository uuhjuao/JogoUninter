#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from code.const import COLOR_GREEN, COLOR_WHITE, MENU_OPTION

from code.const import WIN_WIDTH


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./asset/back3.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        menu_option = 0
        #MenuSound
        pygame.mixer_music.load('./asset/MenuSound2.mp3')  # aqui eu carreago uma música
        pygame.mixer_music.play(-1)  # aqui eu coloco a musica pra tocar e coloco como parameter -1 para tocar repetidamente quando a música acabar
        while True:
            # MenuImage
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(50, "Attack", COLOR_WHITE, ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "on Shinobi", COLOR_WHITE, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_GREEN, ((WIN_WIDTH / 2), 200 + 30 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 200 + 30 * i))
            pygame.display.flip()


            # check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) -1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) -1
                    if event.key == pygame.K_RETURN: # tecla ENTER
                        return MENU_OPTION[menu_option]


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha() #renderiza e cria uma imagem
        text_rect: Rect = text_surf.get_rect(center=text_center_pos) #faz o a moldura(reangulo) para colocar a imagem
        self.window.blit(source=text_surf, dest=text_rect) #dar origem pro destino, desenhar a imagem
