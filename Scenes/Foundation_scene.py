import pygame
from Scenes.Base_scene import Base_scene
from Classes.draw_text import draw_text


class Foundation_scene(Base_scene):
    def __init__(self, screen):
        self.screen = screen
        super().__init__(screen)

    def render(self):
        background = pygame.image.load("Scenes\Background\sfoundation_background1.png").convert_alpha()
        self.screen.blit(background, (0, 0))

        with open('Classes\config.txt', mode='r', encoding='utf-8') as f:
            self.coins = int(f.readline())

        draw_text(self.screen, str(self.coins), 64, 100, 100)

    def add_coin(self):
        self.coins += 1

        # Writing score to file
        with open('Classes\config.txt', mode='w', encoding='utf-8') as f:
            f.write(str(self.coins))

    # annul score
    def cleanup(self):
        with open('Classes\config.txt', mode='w', encoding='utf-8') as f:
            f.write(str(0))
        print('Destroyed')
