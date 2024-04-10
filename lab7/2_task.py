import pygame
pygame.init()

screen = pygame.display.set_mode((400,300))
musics = ['music.mp3','music-2.mp3']
track_index = 0
pygame.mixer.music.load(musics[track_index])
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_DOWN]: pygame.mixer.music.stop()
    if pressed[pygame.K_LEFT]: pygame.mixer.music.play(0)
    if pressed[pygame.K_RIGHT]: track_index = (track_index+1) % len(musics); pygame.mixer.music.load(musics[track_index]); pygame.mixer.music.play()

    screen.fill((255,255,255))
    pygame.display.flip()
pygame.quit()