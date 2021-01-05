import pygame
from Scenes.Base_scene import Base_scene
from Config import config
from Classes.AssetManager import assetManager

# from Classes.Button import Button
from Classes.draw_text import draw_text


class Fight_scene(Base_scene):
    def __init__(self, screen):
        super().__init__(screen)

    def render(self):
        background = assetManager.load_image("fight_background.png")
        get_hero = config.getValue('hero').split('-')[0]
        Hero_JoJo = assetManager.load_image(f"Heros\{get_hero}.png")
        self.get_enemy = config.getValue('enemy').split('-')[0]
        Enemy = assetManager.load_image(f"Antagonists\{self.get_enemy}.png")
        self.screen.blit(background, (0, 0))
        self.screen.blit(Hero_JoJo, (100, 50))
        self.screen.blit(Enemy, (1250, 100))

        super().render('fight_shop')

    def add_hits(self):
        boss_hp = int(config.getValue('enemy').split('-')[1])
        power_hit = int(config.getValue('hero').split('-')[1])
        config.setValue('enemy', self.get_enemy + '-' + str((boss_hp - power_hit)))

