import pygame
from Classes.Scene_manager import Scene_manager

pygame.init()

# Screen setup
size = (1920, 1080)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("JoJo's Cliker")

clock = pygame.time.Clock()
playLs = ['data\Music\Main Theme.wav', 'data\Music\BLOODY STREAM (piano).mp3',
          'data\Music\ost_JoJo_-_Walk_Like_an_Egyptian_65999419.mp3',
          'data\Music\Great_Days_67446269.mp3', 'data\Music\Chase_You_67481061.mp3']
pygame.mixer.music.load(playLs[0])
for i in playLs:
    pygame.mixer.music.queue(i)
pygame.mixer.music.set_volume(0.06)
pygame.mixer.music.play(1)
sound_lose_1 = pygame.mixer.Sound('data\Music\goodbye-jojo.wav')
sound_lose_2 = pygame.mixer.Sound('data\Music\oh-my-god-joseph.wav')
sound_lose_3 = pygame.mixer.Sound('data\Music\muda.wav')
sound_win_1 = pygame.mixer.Sound('data\Music\-wryyyyyyyyy.wav')
sound_win_2 = pygame.mixer.Sound('data\Music\joseph-joestar-nice.wav')
sound_win_3 = pygame.mixer.Sound('data\Music\oraoraoraoraora-sound-effect.wav')
sound_hit = pygame.mixer.Sound('data\Music\e69c35e30a3057.wav')
sound_hit.set_volume(0.35)
# Scene setup
scene_manager = Scene_manager(screen)
# set timer
MYEVENTTYPE = pygame.USEREVENT + 1
pygame.time.set_timer(MYEVENTTYPE, 1000)

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

        if event.type == pygame.KEYDOWN:
            if scene_manager.get_fight().counter == 0:
                scene_manager.get_fight().update_counter()
            if scene_manager.get_fight().win:
                scene_manager.get_fight().set_level()
        # add coin per second
        if scene_manager.get_fight().add_hit:
            sound_hit.play()
            scene_manager.get_fight().red_boos()
        if event.type == MYEVENTTYPE:
            scene_manager.get_fight().timer_fight()
            scene_manager.get_foundation().add_coin_per_sec()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If scene is foundation?
            if scene_manager.get_current_scene_id() == 0:
                if event.button == 1:
                    scene_manager.get_foundation().add_coin()
            # Check if we meed to change scene
            scene_manager.on_click(event.pos)
            scene_manager.set_click_for_buy(True)

        if scene_manager.get_fight().lose:
            if scene_manager.get_fight().level_id == 0:
                sound_lose_1.set_volume(0.1)
                if scene_manager.get_fight().music_counter == 0:
                    sound_lose_1.play(0, 2000)
                    scene_manager.get_fight().music_counter += 1
            elif scene_manager.get_fight().level_id == 1:
                sound_lose_2.set_volume(0.1)
                if scene_manager.get_fight().music_counter == 0:
                    sound_lose_2.play(0, 2000)
                    scene_manager.get_fight().music_counter += 1
            elif scene_manager.get_fight().level_id == 2:
                sound_lose_3.set_volume(0.1)
                if scene_manager.get_fight().music_counter == 0:
                    sound_lose_3.play(0, 4000)
                    scene_manager.get_fight().music_counter += 1

        if scene_manager.get_fight().win:
            if scene_manager.get_fight().level_id == 0:
                sound_win_1.set_volume(0.1)
                if scene_manager.get_fight().music_counter == 0:
                    sound_win_1.play(0, 2000)
                    scene_manager.get_fight().music_counter += 1
            elif scene_manager.get_fight().level_id == 1:
                sound_win_2.set_volume(0.5)
                if scene_manager.get_fight().music_counter == 0:
                    sound_win_2.play(0)
                    scene_manager.get_fight().music_counter += 1
            elif scene_manager.get_fight().level_id == 2:
                sound_win_3.set_volume(0.1)
                if scene_manager.get_fight().music_counter == 0:
                    sound_win_3.play(0, 2000)
                    scene_manager.get_fight().music_counter += 1

    pygame.display.update()
    pygame.display.flip()
    clock.tick(30)
pygame.quit()
