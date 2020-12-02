from Score_Counter import Score_Counter
from Scenes.Speedwagon_scene import Speedwagon_scene
from draw_text import draw_text
from Scenes.Fight_scene import Fight_scene
import pygame



class Init():
    def __init__(self, screen):
        self.fon = Fight_scene(screen, (0, 0))
        self.Score_Counter = Score_Counter(screen, (1350, 100))
        self.jump_button = Speedwagon_scene(screen, (1800, 50))

