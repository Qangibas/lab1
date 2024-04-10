import pygame, random, time
pygame.init()

SIZE = W, H = 1200, 800
FPS = 60
done = False
bg =(0, 0, 0)

screen = pygame.display.set_mode(SIZE, pygame.RESIZABLE)
clock = pygame.time.Clock()

# paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20#*2
paddle = pygame.Rect(W//2-paddleW//2, H - paddleH-30, paddleW, paddleH)
paddle_color = (255, 255, 255)

# ball
ballRadius = 20
ballSpeed = 6#*2
ball_rect = int(ballRadius*2**0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H//2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)


# catching sound
collision_sound = pygame.mixer.Sound('catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top
        
    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# block settings
block_list = [pygame.Rect(10 + 120*i, 50 + 70*j,
            100, 50) for i in range(10)
            for j in range(4)]

# unbreakable bricks
unblreakable_index_list = [random.randrange(0, 40) for i in range(10)]

# bonus bricks
bonus_blocks = [random.randrange(0, 40) for i in range(10)]
for i in bonus_blocks:
    if i in unblreakable_index_list:
        bonus_blocks.remove(i)
        
color_list = [(random.randrange(0, 100), 
               random.randrange(0, 100), 
               random.randrange(0, 255)) 
            for i in range(10) for j in range(4)]

for i in unblreakable_index_list:
    color_list[i] = (255, 255, 255)
    print(i)
for i in bonus_blocks:
    color_list[i] = (255, 255, 0)

# Game over screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetxt = losefont.render('Game over', True, (255, 255, 255))
loserect = losetxt.get_rect()
loserect.center = (W//2, H//2)

# Win screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintxt = winfont.render('You win waw', True, (0, 0, 0))
wintxtRect = wintxt.get_rect()
wintxtRect.center = (W//2, H//2)


# Time
starttime = time.time()
ellapsedtime = starttime - time.time()

# Time screen
timefont = pygame.font.SysFont('comicsansms', 40)
timetxt = timefont.render(f'Time: {ellapsedtime}s', True, (255, 255, 255))
timetxtRect = timetxt.get_rect()
timetxtRect.center = (W/2, 20)



while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # pygame.quit()
            done = True
    screen.fill(bg)

    [pygame.draw.rect(screen, color_list[color], block)
    for color, block in enumerate(block_list)] #drawing blocks
    pygame.draw.rect(screen, paddle_color, paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

 
    # Ball movement
    ball.x +=ballSpeed * dx
    ball.y +=ballSpeed * dy
    
    # Collision left
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    # Collision top
    if ball.centery < ballRadius: # or ball.centery > H - ballRadius:
        dy = -dy
    
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)
        paddle_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    hitIndex = ball.collidelist(block_list)
    # if hitIndex!=-1:
    #     print(hitIndex)

    if hitIndex != -1:
        hitRect = block_list[hitIndex]
        if hitIndex not in unblreakable_index_list:
            hitRect = block_list.pop(hitIndex)
            hitColor = color_list.pop(hitIndex)
            game_score += 1
            collision_sound.play()
            for j in range(len(unblreakable_index_list)):
                if hitIndex < unblreakable_index_list[j]:
                    unblreakable_index_list[j]-=1
            for j in range(len(bonus_blocks)):
                if hitIndex < bonus_blocks[j]:
                    bonus_blocks[j]-=1
                    
            if hitIndex in bonus_blocks:
                bonus_blocks.remove(hitIndex)
                # bonus: 1.2x paddle
                paddleW *=1.2
            dx, dy = detect_collision(dx, dy, ball, hitRect)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
                    
    
    
    # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    # Time
    ellapsedtime = time.time() - starttime
    seconds = int(ellapsedtime)
    timetxt = timefont.render(f'Time: {seconds}s', True, (255, 255, 255))
    screen.blit(timetxt, timetxtRect)
    
    # Ball speed increas
    ballSpeed += ellapsedtime/5000
    
    # Shrink the paddle with time
    paddleW -= ellapsedtime/500
    paddleH = 25
    paddleSpeed = 20
    paddle = pygame.Rect(paddle.x, H - paddleH-30, paddleW, paddleH)
    
    # Win/Lose screen
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetxt, loserect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintxt, wintxtRect)
    
    # Paddle controle
    key = pygame.key.get_pressed()
    
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed
    
    
    pygame.display.update()
    clock.tick(FPS)
