import pygame
from Classes.Scene_manager import Scene_manager

pygame.init()

# Screen setup
size = (1920, 1080)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("JoJo's Cliker")

clock = pygame.time.Clock()

sound = pygame.mixer.Sound('Music\Main Theme.wav')
sound.set_volume(0.01)


# Scene setup
scene_manager = Scene_manager(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # For tests. May be removed
            scene_manager.get_foundation().cleanup()

            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # If scene is foundation?
            if scene_manager.get_current_id() == 0:
                scene_manager.get_foundation().add_coin()
            # Check if we meed to change scene
            scene_manager.set_scene(event.pos)


        sound.play()

    # Rendering scene
    scene_manager.render()

    #  score = Score_Counter(screen)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
