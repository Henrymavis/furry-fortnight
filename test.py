import pygame
print("something else")

pygame.init()
screen = pygame.display.set_mode((600, 400))
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
print("done")
