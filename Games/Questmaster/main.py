import pygame

entities = []

class Entity():
    def __init__(self):
        pass

    def update(self, dt):
        pass

    def render(self, screen):
        pass

def setup():
    pygame.init()
    pygame.display.set_caption("Questserious")
    pygame.mouse.set_visible(1)

def setup_entities():
    pass

def event():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    
    return True

def update(dt):
    for entity in entities:
        if entity is Entity:
            entity.update(dt)

def render(screen):
    for entity in entities:
        if entity is Entity:
            entity.render(screen)
    
def main():
    setup()
    setup_entities()

    screen = pygame.display.set_mode((640, 480))

    clock = pygame.time.Clock()
    
    while True:
        dt = clock.tick(30)

        screen.fill((0,0,0))

        if not event(): return

        update(dt)
        render(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
    print "*** Shutdown ***"
            
