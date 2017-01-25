import interfaces, pygame

class Box(interfaces.Entity):
    def __init__(self):
        interfaces.Entity.__init__(self)

    def update(self, dt):
        pass

class Paddle(interfaces.Entity):
    def __init__(self, speed):
        interfaces.Entity.__init__(self)

        self.speed = speed

    def event(self, evt):
        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_UP:
                self.move(self.rect.x, -self.speed)
            if evt.key == pygame.K_DOWN:
                self.move(self.rect.x, self.speed)
