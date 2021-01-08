import pygame
from Classes.Scene_manager import Scene_manager
from Scenes.Fight_scene import Fight_scene

pygame.init()

# Screen setup
size = (1920, 1080)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("JoJo's Cliker")

clock = pygame.time.Clock()

sound = pygame.mixer.Sound('Music\Main Theme.wav')
sound.set_volume(0.01)
sound.play()

# Scene setup
scene_manager = Scene_manager(screen)
# set timer
MYEVENTTYPE = pygame.USEREVENT + 1
pygame.time.set_timer(MYEVENTTYPE, 1000)
counter = Fight_scene.get_timer()

running = True

while running:
    time = pygame.time.get_ticks() // 1000
    start_time = 0

    # Rendering scene
    point = pygame.mouse.get_pos()
    scene_manager.render(point)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            # For tests. May be removed
            scene_manager.get_foundation().cleanup()

            running = False
        # add coin per second
        if event.type == MYEVENTTYPE:
            counter -= 1
            scene_manager.get_foundation().add_coin_per_sec()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If scene is foundation?
            if scene_manager.get_current_scene_id() == 0:
                if event.button == 1:
                    scene_manager.get_foundation().add_coin()
            # Check if we meed to change scene
            scene_manager.on_click(event.pos)
            scene_manager.set_click_for_buy(True)

    #  score = Score_Counter(screen)
    pygame.display.update()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
