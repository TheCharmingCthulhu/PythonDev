import pygame

class Entity():
    def __init__(self):
        pass

    def event(self, evt):
        pass
    
    def update(self, dt):
        pass

    def render(self, screen):
        screen.blit(self.image, self.rect)

    def image(self, filename, colorkey = None):
        try:
            self.image = pygame.image.load(filename).convert()
            self.rect = self.image.get_rect()
            
            if colorkey is not None:
                if colorkey is -1:
                    colorkey = self.image.get_at((0,0))
                self.image.set_colorkey(colorkey, RLEACCEL)
        except pygame.error, message:
            print "Cannot load image:", filename
            raise SystemExit, message
    
    def move(self, x, y):
        self.rect = self.rect.move(x, y)
