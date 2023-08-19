# First pyGame attempt
# Dino game initial code
# Example file showing a basic pygame "game loop"
import pygame, os, time, random

# size
WIDTH = 1280
HEIGHT= 720

# frames for animation of dino
# walking
dinoWalkFrames = ["Walk (1).png",
                  "Walk (2).png",
                  "Walk (3).png",
                  "Walk (4).png",
                  "Walk (5).png"]
# idle
dinoFrames = ["Idle (1).png",
              "Idle (2).png",
              "Walk (1).png",
              "Walk (2).png"]
currentFrame = 0

# player image
DINO = pygame.image.load(os.path.join("assets", dinoFrames[currentFrame]))
print(DINO)
# enemies
PTERA = pygame.image.load(os.path.join("assets", "tera1.png"))

# projectile
CLAW = pygame.image.load(os.path.join("assets", "claw.png"))

# background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets",
                                                           "mainBg.png")),
                                                           (1280, 720))

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
noOfWeapons = 5
enemies = []
waveLen = 5
enemyVel = 2
vel = 7
mode = 0
count = 0   

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
        self.allSprites = [pygame.image.load("Assets/Idle (1).png"),
                           pygame.image.load("Assets/Idle (2).png"),
                           pygame.image.load("Assets/Walk (1).png"),
                           pygame.image.load("Assets/Walk (2).png")]
        self.currentSprite = 2
        self.spriteImage = self.allSprites[self.currentSprite]
        self.maxHealth = health

    def collision(self, obj):
        return collide(obj, self)
    
    def updateImage(self, frame):
        self.spriteImage = self.allSprites[frame] 
        
    def animate(self, mode, count):
        counter = count
        if counter >= 4:
            counter = 0
        if mode == 1 and int(counter) == 0:
            newFrame = 2
            self.updateImage(newFrame)
        if mode == 1 and int(counter) == 1:
            newFrame = 3
            self.updateImage(newFrame)
        if mode == 2 and int(counter) == 0:
            newFrame = 2
            self.updateImage(newFrame)
        if mode == 2 and int(counter) == 1:
            newFrame = 3
            self.updateImage(newFrame)
        counter += 0.2
        return counter    
    
myDino = Player(50, 565)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            mode = 0

    
    for enemy in enemies:
        enemy.draw(screen)
    
    #curentFrame, count = updateFrame(mode, count)
    #currentFrame += 0.1
    #if int(currentFrame) > 3:
    #    currentFrame = 0
    
    #DINO = pygame.image.load(os.path.join("assets", dinoIdleFrames[currentFrame]))
    count = myDino.animate(mode, count)
    myDino.draw(screen)    

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
    
    pygame.display.update()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000
        
pygame.quit()