from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
import pygame

def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill((0, 0, 0))
        
        updatable.update(dt)
        
        for each in drawable: 
            each.draw(screen)
        
        pygame.display.flip()
        dtSeconds = clock.tick(60)
        dt = dtSeconds / 1000.0

if __name__ == "__main__":
    main()
