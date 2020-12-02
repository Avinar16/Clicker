import pygame
from Classes.draw_text import draw_text


class Score_Counter:
    def __init__(self, screen):
        # Reading score from file
        with open('Classes\config.txt', mode='r', encoding='utf-8') as f:
            self.coins = int(f.readline())

        self.screen = screen
        # Rendering score
        draw_text(self.screen, str(self.coins), 64, 500, 100)



    def add_coin(self):
        self.coins += 1

        print(self.coins)
        with open('Classes\config.txt', mode='w', encoding='utf-8') as f:
            f.write(str(self.coins))


    def cleanup(self):
        with open('Classes\config.txt', mode='w', encoding='utf-8') as f:
            f.write(str(0))



