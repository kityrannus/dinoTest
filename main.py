# First pyGame attempt
# Dino game initial code
# Example file showing a basic pygame "game loop"
import pygame, os, time, random

# size
WIDTH = 1280
HEIGHT= 720

# frames for animation of dino
# walking
dinoWalkFrames = ["Walk (1).png", "Walk (2).png", "Walk (3).png", "Walk (4).png", "Walk (5).png"]
# idle
dinoFrames = ["Idle (1).png", "Idle (2).png", "Walk (1).png", "Walk (2).png"]
currentFrame = 0

# player image
DINO = pygame.image.load(os.path.join("assets", dinoFrames[currentFrame]))
print(DINO)
# enemies
PTERA = pygame.image.load(os.path.join("assets", "tera1.png"))

# projectile
CLAW = pygame.image.load(os.path.join("assets", "claw.png"))

# background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "mainBg.png")), (1280, 720))

# pygame setup
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
newScreen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Adventure")
clock = pygame.time.Clock()
pygame.font.init()
mainFont = pygame.font.SysFont("Arial", 60)
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
level = 1
score = 0
health = 100
noOfWeapons = 5
enemies = []
waveLen = 5
enemyVel = 2
vel = 7
mode = 0
count = 0

def updateFrame(mod, counter):
    act = 0
    if int(counter) >= 5:
        counter = 0
    if mod == 0:
        if counter <1:
            act = 0
        elif counter >= 2:
            act = 1
    if mod == 1:
        if counter <30.0:
            act = 2
        elif 30 <= counter < 60:
            act = 3
    if mod == 2:
        if counter <30.0:
            act = 4
        elif 30 <= counter < 60:
            act = 5
    counter += 0.2
    #print(act, counter)
    return act, counter
    
    
def collide(self, obj2):
        offset_x = obj2.x - self.x
        offset_y = obj2.y - self.y
        return self.mask.overlap(obj2.mask, (offset_x, offset_y)) != None

class Projectile:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)

    def draw(self, window):
        window.blit(self.img, (self.x, self.y))

    def move(self, vel):
        self.y -= vel

    def off_screen(self, height):
        return not(self.y <= height and self.y >= 0)

    def collision(self, obj):
        return collide(obj, self)

class Sprite:
    def __init__(self, x, y, health = 100):
        self. x = x
        self.y = y
        self.health = health
        self.spriteImage = None

    def draw(self, window):
        window.blit(self.spriteImage, (self.x, self.y))

    def getWidth(self):
        return self.spriteImage.get_width()

    def getHeight(self):
        return self.spriteImage.get_height()

class Player(Sprite):
    def __init__(self, x, y, health = 100):
        super().__init__(x, y, health)
        self.allSprites = [pygame.image.load("Assets/Idle (1).png"), pygame.image.load("Assets/Idle (2).png"), pygame.image.load("Assets/Walk (1).png"), pygame.image.load("Assets/Walk (2).png")]
        self.currentSprite = 2
        self.spriteImage = self.allSprites[self.currentSprite]
        self.fire = CLAW
        self.attacks = []
        for missile in range(1):
            missile = Projectile(self.x, self.y, self.fire)
            self.attacks.append(missile)
        self.mask = pygame.mask.from_surface(self.spriteImage)
        self.maxHealth = health

    def collision(self, obj):
        return collide(obj, self)
    
    def updateImage(self, frame):
        self.spriteImage = self.allSprites[frame]
        
    def animate(self, mode):
        counter = 0.0
        if mode == 0 and int(counter) == 0:
            self.updateImage(0)
        if mode == 0 and int(counter) == 1:
            self.updateImage(1)
        counter += 0.1

    def shoot(self):
        missile = Projectile(self.x + 80, self.y + 75, self.fire)
        self.attacks.append(missile)
        missile.draw(screen)

    def moveAttack(self, obj):
        print(len(self.attacks))
        for missile in self.attacks:
            missile.move(vel)
            missile.draw(screen)
            if missile.y < 0:
                self.attacks.remove(missile)
            

class Enemy(Sprite):
    def __init__(self, x, y, health = 50):
        super().__init__(x, y, health)
        self.spriteImage = PTERA
        self.mask = pygame.mask.from_surface(self.spriteImage)
        maxHealth = health

    def move(self, vel):
        self.x -= vel
    
myDino = Player(50, 565)
enemy1 = Enemy(720, 50)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            mode = 0


    levelLabel = mainFont.render(f"Level: {level}", 1, (255, 0, 0))
    healthLabel = mainFont.render(f"Health: {health}", 1, (255, 0, 0))
    screen.blit(BG, (0, 0))
    screen.blit(levelLabel, (300, 5))
    screen.blit(healthLabel, (WIDTH - healthLabel.get_width(), 5))
    
    for enemy in enemies:
        enemy.draw(screen)
    
    #curentFrame, count = updateFrame(mode, count)
    currentFrame += 0.1
    if int(currentFrame) > 3:
        currentFrame = 0
    
    #DINO = pygame.image.load(os.path.join("assets", dinoIdleFrames[currentFrame]))
    myDino.updateImage(int(currentFrame))
    myDino.draw(screen)
    
    if len(enemies) == 0:
        level += 1
        waveLen += 2
        for i in range(waveLen):
            enemy = Enemy(random.randrange(50, WIDTH + 100),random.randrange(-50, 200))
            enemies.append(enemy)


    # get key presses
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and myDino.y - 60 > 0 :
        myDino.y -= 300 *dt
    if keys[pygame.K_s] and myDino.y + myDino.getHeight() < HEIGHT:
        myDino.y += 300 *dt
    if keys[pygame.K_a] and myDino.x - 50 > 0:
        mode = 1 #left
        myDino.x -= 300 *dt
    if keys[pygame.K_d] and myDino.x + myDino.getWidth() < WIDTH:
        mode = 2 # right
        myDino.x += 300 *dt
    if keys[pygame.K_SPACE]:
        myDino.shoot()
    
    

    myDino.moveAttack(enemies)

    for enemy in enemies:
        enemy.move(enemyVel)

        if enemy.x < 50:
            enemies.remove(enemy)
            
        if myDino.collision(enemy):
            health -=5
            enemies.remove(enemy)
        
        if len(myDino.attacks) > 0:
            if myDino.attacks[0].collision(enemy):
                score += 1
                enemies.remove(enemy)
    
            

    
    pygame.display.update()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
        
pygame.quit()