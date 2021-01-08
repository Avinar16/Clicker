from Scenes.Base_scene import Base_scene
from Config import config
from Classes.AssetManager import assetManager
from Classes.draw_text import draw_text


class Fight_scene(Base_scene):
    def __init__(self, screen):
        self.counter = 30
        self.check_fight = False
        self.get_hero = config.getValue('hero')
        self.background = assetManager.load_image("fight_background.png")
        self.black_fone = assetManager.load_image("black_fone.jpg")
        self.Hero_JoJo = assetManager.load_image(f"Heros\{self.get_hero}.png")
        self.get_enemy = config.getValue('enemy').split('/')[0]
        self.Enemy = assetManager.load_image(f"Antagonists\{self.get_enemy}.png")
        super().__init__(screen)

    def render(self):
        self.boss_hp = int(config.getValue('enemy').split('/')[1])
        if self.boss_hp <= 0 :
            self.player_win()
        elif self.counter == 0:
            self.player_lose()
        else:
            self.screen.blit(self.background, (0, 0))
            self.screen.blit(self.Hero_JoJo, (100, 50))
            self.screen.blit(self.Enemy, (1250, 100))
            self.buttons.empty()
            self.buttons.generate('ramka', start_x=550, start_y=700)
            self.buttons.draw(self.screen)
            if self.check_fight:
                draw_text(self.screen, str(self.counter), 64, 900, 100, font=True)
                draw_text(self.screen, 'Boss hp:', 50, 1700, 900, font=True)
                draw_text(self.screen, str(self.boss_hp), 50, 1750, 950, font=True)
        super().render('fight_shop')

    def add_hits(self):
        power_hit = int(config.getValue('damage'))
        config.setValue('enemy', self.get_enemy + '/' + str((self.boss_hp - power_hit)))

    def activate_timer(self):
        self.check_fight = True

    def timer_fight(self):
        if self.counter == 0:
            pass
        else:
            if self.check_fight:
                self.counter -= 1

    def player_lose(self):
        self.screen.blit(self.black_fone, (0, 0))
        draw_text(self.screen, 'YOU LOSE TRY AGAIN, PRESS ANY KEY TO CONTINUE', 60, 900, 100, font=True)


    def update_counter(self):
        self.counter = 30

    def player_win(self):
        self.screen.blit(self.black_fone, (0, 0))
        draw_text(self.screen, 'YOU WIN, PRESS ANY KEY TO NEXT LEVEL', 60, 900, 100, font=True)









