import pygame

class Entity():
    def __init__(self):
        self.tag = None

    def event(self, evt, ents):
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

    def collide(self, target):
        if self is target: return

        offset = 2
        sides = []
    
        if isinstance(target, Entity):
            if target.rect.bottom + offset > self.rect.top and target.rect.top < self.rect.top: sides.append("T")
            if target.rect.top - offset < self.rect.bottom and target.rect.bottom > self.rect.bottom: sides.append("B")
            #if target.rect.right < self.rect.left and target.rect.right > self.rect.left: sides.append("L")
            #if target.rect.left > self.rect.right and target.rect.left < self.rect.left: sides.append("R")

        return sides

    def collision(self, targets):
        for target in targets:
            if self is not target:
                if len(self.collide(target)) > 0:
                    return self.collide(target)
        return []
            
