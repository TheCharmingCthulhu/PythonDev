import pygame
import entities, interfaces

ents = [] # global entity list
resolution = (640, 480) # resolution

def setup(): # Initialize pygame
    pygame.init()
    pygame.mouse.set_visible(1)
    pygame.key.set_repeat(1, 10)
    return pygame.display.set_mode(resolution)

def construct(): # Initialize entities
    for y in (0, resolution[1] - 32): # define border
        for x in range(resolution[0] / 32):
            wall = entities.Box()
            wall.image("images/box.png")
            wall.move(x * wall.rect.width, y)

            ents.append(wall)

    paddle = entities.Paddle(5)
    paddle.image("images/paddle.png")
    paddle.move(0, (resolution[1] / 2) - (paddle.rect.height / 2))
    paddle.tag = "paddle_player"
    ents.append(paddle)

    bot = entities.Bot(5)
    bot.image("images/paddle.png")
    bot.move(resolution[0] - bot.rect.width, (resolution[1] / 2) - (bot.rect.height / 2))
    bot.tag = "paddle_bot"
    ents.append(bot)

    ball = entities.Ball()
    ball.image("images/ball.png")
    ball.move((resolution[0] / 2) - (ball.rect.width / 2), (resolution[1] / 2) - (ball.rect.height / 2))
    ball.tag = "ball"
    ents.append(ball)

def foreach_entity(func_name, *args): # apply on all entities
    for ent in ents:
        if isinstance(ent, interfaces.Entity): # check's instance
            getattr(ent, func_name)(*args) # retrievs method by string and calls it while unpacking tuple

def find_entity(name):
    for ent in ents:
        if ent.tag == name:
            return ent
        
def event(evt): # event-check entities
    if evt.type == pygame.QUIT:
        return False
    elif evt.type == pygame.KEYDOWN:
        if evt.key == pygame.K_ESCAPE:
            return False

    foreach_entity("event", evt, ents)
    
    return True

def update(dt): # update entities
    foreach_entity("update", dt, ents)
    
def render(screen): # render entities
    foreach_entity("render", screen)

def main():
    screen = setup()

    construct() # initialization of various game objects that are active on the scene

    clock = pygame.time.Clock()
    
    while True:
        dt = clock.tick(60) # framerate limit : returns deltatime
        bg = pygame.Surface(screen.get_size()).convert() # background creation
        bg.fill((0, 0, 0)) # fill background
        screen.blit(bg, (0, 0)) # blit background

        for evt in pygame.event.get():
            if not event(evt): return # check and process events

        update(dt) # update entities
        render(screen) # render entities

        pygame.display.set_caption(str(clock.get_fps()))
        pygame.display.update()
        pygame.display.flip()

if __name__ == "__main__":
    main()
