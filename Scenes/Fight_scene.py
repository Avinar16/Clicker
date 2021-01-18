from Scenes.Base_scene import Base_scene
from Config import config
from Classes.AssetManager import assetManager
from Classes.draw_text import draw_text
from Classes.check_level import check_level, set_level
from os import startfile
from math import ceil


class Fight_scene(Base_scene):
    def __init__(self, screen):
        self.win = False
        self.lose = False
        self.level_id = check_level()
        self.music_counter = 0
        self.counter = 30
        self.add_hit = False
        self.check_fight = False
        self.background = assetManager.load_image("fight_background.png")
        self.black_fone = assetManager.load_image("black_fone.jpg")
        self.boss_hp_start = int(config.getValue('enemy').split('/')[1])
        super().__init__(screen)

    def render(self):
        if self.level_id == 0:
            self.background = assetManager.load_image("levels\level1.png")
        elif self.level_id == 1:
            self.background = assetManager.load_image("levels\level2.png")
        elif self.level_id == 2:
            self.background = assetManager.load_image("levels\level3.png")
        self.get_hero = config.getValue('hero')
        # self.Hero_JoJo = assetManager.load_image(f"Heros\{self.get_hero}.png")
        self.boss_hp = int(config.getValue('enemy').split('/')[1])
        self.get_enemy = config.getValue('enemy').split('/')[0]
        # self.Enemy = assetManager.load_image(f"Antagonists\{self.get_enemy}.png")
        # self.Enemy_red = assetManager.load_image(f"Antagonists\{self.get_enemy + '_' + str(self.level_id)}.png")
        if self.boss_hp <= 0:
            self.player_win()
        elif self.counter == 0:
            self.player_lose()
        else:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(assetManager.load_image(f"Heros\{self.get_hero}.png"), (100, 100))
            self.screen.blit(assetManager.load_image(f"Antagonists\{self.get_enemy}.png"), (1250, 100))
            self.buttons.empty()
            self.buttons.generate('attack_button', start_x=800, start_y=700)
            self.buttons.draw(self.screen)
            if self.check_fight:
                draw_text(self.screen, str(self.counter), 64, 900, 100, font=True)
                draw_text(self.screen, 'Boss hp:', 50, 1700, 900, font=True)
                draw_text(self.screen, str(self.boss_hp), 50, 1750, 950, font=True)
        if self.level_id == 0:
            super().render('fight_shop')
        elif self.level_id == 1:
            super().render('fight_shop_level1')
        elif self.level_id == 2:
            super().render('fight_shop_level2')

    def add_hits(self):
        if self.check_fight:
            self.add_hit = True
            power_hit = int(config.getValue('damage'))
            config.setValue('enemy', self.get_enemy + '/' + str((self.boss_hp - power_hit)))

    def get_win(self):
        return self.win

    def red_boos(self):
        self.add_hit = False
        if not self.win:
            self.screen.blit(assetManager.load_image(f"Antagonists\{self.get_enemy + '_' + str(self.level_id)}.png"),
                             (1250, 100))

    def activate_timer(self):
        self.check_fight = True

    def timer_fight(self):
        if self.counter == 0:
            pass
        else:
            if self.check_fight:
                self.counter -= 1

    def player_lose(self):
        self.lose = True
        self.screen.blit(self.black_fone, (0, 0))
        draw_text(self.screen, 'YOU LOSE TRY AGAIN, PRESS SPACE TO CONTINUE', 60, 900, 100, font=True)

    def update_counter(self):
        self.check_fight = False
        self.counter = 30
        self.lose = False
        config.setValue('enemy', self.get_enemy + '/' + str(self.boss_hp_start))
        self.stop_music()

    def stop_music(self):
        self.music_counter = 0

    def player_win(self):
        self.check_fight = False
        self.counter = 30
        self.win = True
        self.screen.blit(self.black_fone, (0, 0))
        if self.level_id != 2:
            draw_text(self.screen, 'YOU WIN, PRESS SPACE TO NEXT LEVEL', 60, 900, 100, font=True)
        else:
            draw_text(self.screen, 'CONGRATULATIONS, PRESS SPACE TO CONTINUE', 60, 900, 100, font=True)
            startfile('data\Credits\Credits.mp4')
            config.load_preset()

    def set_level(self):
        if self.level_id == 2:
            pass
        else:
            cur_pps = int(config.getValue('pps'))
            config.setValue('pps', ceil(cur_pps * 1.5))
            self.level_id += 1
            set_level(self.level_id)
        if self.level_id == 1:
            config.setValue('hero', 'Joseph')
            config.setValue('enemy', 'Kars/20000')
        elif self.level_id == 2:
            config.setValue('hero', 'Jotaro')
            config.setValue('enemy', 'DIO/50000')
        self.stop_music()
        self.win = False
