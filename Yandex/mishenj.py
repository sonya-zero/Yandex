import pygame



try:
    d = [int(i) for i in input().split()]
except:
    print("Неправильный формат ввода")
    exit()

def drawl():
    r = width // 2
    screen.fill((0, 0, 0))
    if n % 3 == 0:
        for i in range(n):
            if i % 3 == 2:
                pygame.draw.circle(screen, (255, 0, 0), (width // 2, height // 2), r)
            elif i % 3 == 1:
                pygame.draw.circle(screen, (0, 255, 0), (width // 2, height // 2), r)
            elif i % 3 == 0:
                pygame.draw.circle(screen, (0, 0, 255), (width // 2, height // 2), r)
            r = r - w

    elif n % 3 == 1:
        for i in range(n):
            if i % 3 == 0:
                pygame.draw.circle(screen, (255, 0, 0), (width // 2, height // 2), r)
            elif i % 3 == 2:
                pygame.draw.circle(screen, (0, 255, 0), (width // 2, height // 2), r)
            elif i % 3 == 1:
                pygame.draw.circle(screen, (0, 0, 255), (width // 2, height // 2), r)
            r = r - w

    else:
        for i in range(n):
            if i % 3 == 1:
                pygame.draw.circle(screen, (255, 0, 0), (width // 2, height // 2), r)
            elif i % 3 == 2:
                pygame.draw.circle(screen, (0, 255, 0), (width // 2, height // 2), r)
            elif i % 3 == 0:
                pygame.draw.circle(screen, (0, 0, 255), (width // 2, height // 2), r)
            r = r - w


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption("")
    w = int(d[0])
    n = int(d[1])
    size = width, height = (w * n * 2), (2 * w * n)
    screen = pygame.display.set_mode(size)
    drawl()
    pygame.display.flip()
    while pygame.event.wait().type != pygame.QUIT:
        pass
    pygame.quit()