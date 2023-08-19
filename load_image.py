import os
import pygame

main_dir = os.path.split(os.path.abspath(__file__))[0]
data_fir = os.path.join(main_dir, "data")

def loadImage(name, colorKey = None):
    fullName = os.path.join(data_dir, name)
    try:
        image = pygame.image.load(fullName)
    except pygame.error:
        print("Unable to load image", fullName)
        raise SystemExit(str(pygame.get_error()))
    image= image.convert()
    if colorKey is not None:
        colorKey = image.get_at((0, 0))
    image.set_colorkey(colorKey, pygame.RLEAACCEL)
    
    return image, image.get_rect()


