from Classes.Score_Counter import Score_Counter
from Scenes.Speedwagon_scene import Speedwagon_scene
from Classes.draw_text import draw_text
from Scenes.Fight_scene import Fight_scene
import pygame



class Init():
    def __init__(self, screen):
        self.fon = Fight_scene(screen, (0, 0))


