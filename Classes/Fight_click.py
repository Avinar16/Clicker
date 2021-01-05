from Classes.Scene_manager import Scene_manager
from Config import config

class fight:
    def __init__(self):
        self.allow_attack = False
        if Scene_manager.get_current_scene_id() == 1:
            self.allow_attack = True

    def add_hits(self):
        if self.hit == True and self.allow_attack == True:
            boss_hp = int(config.config.getValue('enemy').split('-')[1])
            power_hit = int(config.config.getValue('hero').split('-')[1])
            print(boss_hp, power_hit)
            boss_hp -= power_hit
            self.hit = False
            print(1)