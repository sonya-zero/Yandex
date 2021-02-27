import pygame

def move():
    # print(event.pos)
    screen2.fill("black")
    pygame.draw.circle(screen2, color, circle, 20)
    screen.blit(screen2, (0, 0))

if __name__ == "__main__":
    pygame.init()
    size = width, height = 501, 501
    screen = pygame.display.set_mode(size)
    screen.fill(pygame.Color("black"))
    screen2 = pygame.Surface(screen.get_size())
    running = True
    color = pygame.Color("red")
    circle = [255, 255]
    velocity = [0, 0]
    pygame.draw.circle(screen, color, circle, 20)
    target = circle
    clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == 256:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            target = event.pos
    if target[0] > circle[0]:
        velocity[0] = 1
    elif target[0] < circle[0]:
        velocity[0] = -1
    else:
        velocity[0] = 0
    if target[1] > circle[1]:
        velocity[1] = 1
    elif target[1] < circle[1]:
        velocity[1] = -1
    else:
        velocity[1] = 0
    circle[0], circle[1] = circle[0] + velocity[0], circle[1] + velocity[1]
    move()
    clock.tick(50)
    pygame.display.flip()
pygame.quit()