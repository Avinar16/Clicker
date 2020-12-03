import pygame
from Scenes.Base_scene import Base_scene
from Config import Config

#from Classes.Button import Button
from Classes.draw_text import draw_text


class Fight_scene(Base_scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.this_confing = Config()

    def render(self):
        background = pygame.image.load("Scenes\Background\Back.png").convert_alpha()
        Hero_JoJo = pygame.image.load("Characters\Heros\Jonatan.png").convert_alpha()
        get_enemy = self.this_confing.getValue('enemy')
        Enemy = pygame.image.load(f"Characters\Antagonists\{get_enemy}.png").convert_alpha()
        self.screen.blit(background, (0, 0))
        self.screen.blit(Hero_JoJo, (100, 50))
        self.screen.blit(Enemy, (1250, 100))

        super().render('fight_shop')

