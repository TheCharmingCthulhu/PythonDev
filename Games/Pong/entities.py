import interfaces, pygame

class Box(interfaces.Entity):
    def __init__(self):
        interfaces.Entity.__init__(self)

class Ball(interfaces.Entity):
    def __init__(self):
        interfaces.Entity.__init__(self)

        self.freeze()

    def event(self, evt, ents):
        if evt.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            self.launch(-3, 5)
        
    def update(self, dt, ents):    
        print self.collision(ents)
    
        if "TL" in self.collision(ents) or "TR" in self.collision(ents) or \
           "BL" in self.collision(ents) or "BR" in self.collision(ents):
            self.speed[1] = -self.speed[1]

        if "TL" in self.collision(ents) or "BL" in self.collision(ents) or \
           "TR" in self.collision(ents) or "BR" in self.collision(ents):
            self.speed[0] = -self.speed[0]

        print self.collision(ents)
        
        self.move(self.speed[0], self.speed[1])
        
    def launch(self, x, y):
        self.speed = [x, y]

    def freeze(self):
        self.speed = [0, 0]

class Paddle(interfaces.Entity):
    def __init__(self, speed):
        interfaces.Entity.__init__(self)

        self.speed = speed

    def event(self, evt, ents):
        print self.collision(ents)
        
        if evt.type == pygame.KEYDOWN:
            if evt.key == pygame.K_UP:
                if "TL" not in self.collision(ents) and "TR" not in self.collision(ents):
                    self.move(0, -self.speed)
            if evt.key == pygame.K_DOWN:
                if "BL" not in self.collision(ents) and "BR" not in self.collision(ents):
                    self.move(0, self.speed)

class Bot(Paddle):
    def __init__(self, speed):
        Paddle.__init__(self, speed)
        
    def update(self, dt, ents):
        pass

    def event(self, evt, ents):
        pass
