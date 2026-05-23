import pygame
import sys

pygame.init()
# Use standard Android display flags
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN | pygame.SCALED)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    screen.fill((20, 30, 40)) # Dark blue background
    
    # Draw a green placeholder box in the center
    w, h = screen.get_size()
    pygame.draw.rect(screen, (0, 255, 0), (w//4, h//4, w//2, h//2))
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
