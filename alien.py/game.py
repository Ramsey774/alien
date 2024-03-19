import pygame
import os

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Alien Shooter")


WHITE = (255, 255, 255)
RED = (255, 0, 0)


FPS = 60
VEL = 5
BULLET_VEL = 7
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40




YELLOW_SPACESHIP_IMAGE = pygame.image.load(
    os.path.join('asset', 'spaceship_yellow.png'))
YELLOW_SPACESHIP = pygame.transform.rotate(
    pygame.transform.scale(
    YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)


SPACE = pygame.transform.scale(pygame.image.load(
    os.path.join('asset', 'Space-Background-Image-2.jpg')), (WIDTH, HEIGHT))

def draw_window(yellow, yellow_bullets):
     WIN.blit(SPACE, (0, 0))
     WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))

     for bullet in yellow_bullets:
         pygame.draw.rect(WIN, RED, bullet)
     
     pygame.display.update()

def yellow_movement(keys_pressed, yellow):
        if keys_pressed[pygame.K_UP] and yellow.y - VEL > 0: #UP
            yellow.y -= VEL
        if keys_pressed[pygame.K_DOWN] and yellow.y + VEL + yellow.width < HEIGHT: #DOWN
            yellow.y += VEL  


def handle_bullets(yellow_bullets, yellow):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL


def main():
    yellow = pygame.Rect(50, 200, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    yellow_bullets = []
    
    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.KEYDOWN:
                 if event.key == pygame.K_SPACE:
                    bullet = pygame.Rect(
                        yellow.x + yellow.width, yellow.y + yellow.height//2 - 2, 10, 5)
                    yellow_bullets.append(bullet) 


               

        keys_pressed = pygame.key.get_pressed()
        yellow_movement(keys_pressed, yellow)

        handle_bullets(yellow_bullets, yellow)
         
       
        
        
        draw_window(yellow, yellow_bullets)
    
    
    
    pygame.quit()

if __name__ == "__main__":
    main()




