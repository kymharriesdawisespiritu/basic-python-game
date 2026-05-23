import pygame
import sys

pygame.init()
# Setup scalable full screen for mobile
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.SCALED)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    # Fill the screen with solid RED
    screen.fill((255, 0, 0)) 
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
