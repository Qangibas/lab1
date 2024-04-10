import pygame

pygame.init()
screen = pygame.display.set_mode((1000,750))

image = pygame.image.load("mainclock.png")
image1 = pygame.image.load("leftarm.png")
image2 = pygame.image.load("rightarm.png")

image = pygame.transform.scale(image, (1000,750))
image1 = pygame.transform.scale(image1, (70, 620))
image2 = pygame.transform.scale(image2, (1000, 750))

clock = pygame.time.Clock()
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    
    screen.fill((255,255,255))

    now = pygame.time.get_ticks() / 1000

    seconds = (now%60) *6
    minutes =  (now/60 % 60) *6
    
    rotated_image1 = pygame.transform.rotate(image1, -seconds)
    rotated_image2 = pygame.transform.rotate(image2, -minutes)

    new_rect1 = rotated_image1.get_rect(center = image.get_rect(center = (505, 390)).center)
    new_rect2 = rotated_image2.get_rect(center = image.get_rect(center = (500, 375)).center)

    screen.blit(image, (0,0))
    screen.blit(rotated_image1, new_rect1)
    screen.blit(rotated_image2, new_rect2)
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()