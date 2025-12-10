from player import Player
import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state


def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    ## Initialize pygame
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    # Crate our sprite groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    
    # Add a player instance
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    
    # Main game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
        
        # Update Sprites
        updatable.update(dt)
        
        screen.fill("black")
        
        # Draw Sprites
        for sprite in drawable:
            sprite.draw(screen)
        
        # Update the display
        pygame.display.flip()
        
        # Cap the frame rate and calculate delta time
        dt = clock.tick(60) / 1000  # Delta time in seconds



if __name__ == "__main__":
    main()
