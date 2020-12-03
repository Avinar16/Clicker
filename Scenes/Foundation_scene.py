import pygame
from Scenes.Base_scene import Base_scene
from Classes.draw_text import draw_text
from Config import Config


class Foundation_scene(Base_scene):
    def __init__(self, screen):
        self.screen = screen
        self.this_confing = Config()
        super().__init__(screen)

    def render(self):
        background = pygame.image.load("Scenes\Background\sfoundation_background1.png").convert_alpha()
        self.screen.blit(background, (0, 0))
        self.coins = int(self.this_confing.getValue('coins'))
        draw_text(self.screen, str(self.coins), 64, 100, 100)

    def add_coin(self):
        self.coins += 1
        # Writing score to file
        self.this_confing.setValue('coins', str(self.coins))


    # annul score
    def cleanup(self):
        self.this_confing.setValue('coins', 0)
        print('Destroyed')
