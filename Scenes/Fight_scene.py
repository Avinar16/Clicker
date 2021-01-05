import pygame
from Scenes.Base_scene import Base_scene
from Config import Config
from Classes.AssetManager import assetManager

#from Classes.Button import Button
from Classes.draw_text import draw_text


class Fight_scene(Base_scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.this_confing = Config('config.csv')

    def render(self):
        background = assetManager.load_image("fight_background.png")
        get_hero = self.this_confing.getValue('hero')
        Hero_JoJo = assetManager.load_image(f"Heros\{get_hero}.png")
        get_enemy = self.this_confing.getValue('enemy').split('-')
        Enemy = assetManager.load_image(f"Antagonists\{get_enemy[0]}.png")
        self.screen.blit(background, (0, 0))
        self.screen.blit(Hero_JoJo, (100, 50))
        self.screen.blit(Enemy, (1250, 100))

        super().render('fight_shop')

