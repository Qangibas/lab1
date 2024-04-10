import pygame, sys, random
import time

pygame.init()
clock = pygame.time.Clock()
FPS = 60
SIZE = WIDTH, HEIGHT = 800, 600
SPEED = 5
LEVEL = 0
SCORE = 0
COINS = 0
backgraund = pygame.image.load("AnimatedStreet.png")
backgraund = pygame.transform.scale(backgraund, (WIDTH, HEIGHT))
font = pygame.font.SysFont('Verdana', 60)
font_small = pygame.font.SysFont('Verdana', 20)
game_over = font.render('Game over', True, (0, 0, 0))
game_over_rect = game_over.get_rect()
game_over_rect.center = (WIDTH//2, HEIGHT//2)

screen = pygame.display.set_mode(SIZE)
screen.fill("White")
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40), 0)
    def move(self):
        self.rect.move_ip(0, SPEED)
        global SCORE
        if (self.rect.bottom > HEIGHT):
            SCORE += 1
            self.rect.center = (random.randint(40, WIDTH-40), -100)
            
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_LEFT]:
                self.rect.move_ip(-SPEED, 0)
        if self.rect.right < WIDTH:
            if pressed_keys[pygame.K_RIGHT]:
                self.rect.move_ip(SPEED, 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.randomcoin = random.randint(1, 3)
        self.image = pygame.image.load(f"coin{self.randomcoin}.png")
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(20, HEIGHT-20), 0)
    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > HEIGHT:
            self.rect.center = (random.randint(40, HEIGHT-40), 0)
        
        
P1 = Player()
E1 = Enemy()
COIN = Coin()

enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(COIN)
all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(COIN)
all_sprites.add(P1)

def leveladder():
    global LEVEL
    global SPEED
    if (COINS)//4 > LEVEL:
        LEVEL += 1
        SPEED += 1



while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(backgraund, (0, 0))
    # screen.blit(backgraund, (400, 0))
    scores = font_small.render(str(SCORE), True, (0, 0, 0))    
    screen.blit(scores, (10, 10))
    collected = font_small.render(str(COINS), True, (0, 0, 0))
    screen.blit(collected, (HEIGHT-30, 10))
    levels = font_small.render(str(LEVEL), True, (0, 0, 0))
    screen.blit(levels, (HEIGHT//2, 10))

    for i in all_sprites:
        i.move()
        screen.blit(i.image, i.rect)
    
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(1)
        
        screen.fill('Red')
        screen.blit(game_over, game_over_rect)
        
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()
    
    if pygame.sprite.spritecollideany(P1, coins):
        pygame.mixer.Sound('collect.wav').play()
        for coin in coins:
            coin.kill()
        if COIN.randomcoin == 1:
            COINS += 1
        if COIN.randomcoin == 2:
            COINS += 2
        if COIN.randomcoin == 3:
            COINS += 3
    
    if len(coins) == 0:
        COIN = Coin()
        coins.add(COIN)
        all_sprites.add(COIN)
    leveladder()
    
    pygame.display.update()
    clock.tick(FPS)