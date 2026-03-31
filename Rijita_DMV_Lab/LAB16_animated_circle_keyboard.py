import pygame
import sys
pygame.init()
# User input
radius = int(input("Enter the size (radius) of the circle: "))
speed = int(input("Enter the speed of the circle: "))
# Screen size
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Circle Movement with X and Y Axis")
# Starting position
x = width // 2
y = height // 2
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    # Key press detection
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    screen.fill((255,255,255))
    # Draw X axis
    pygame.draw.line(screen,(0,0,0),(0,height//2),(width,height//2),2)
    # Draw Y axis
    pygame.draw.line(screen,(0,0,0),(width//2,0),(width//2,height),2)
    # Draw axis numbers
    for i in range(0,width,100):
        text = font.render(str(i-width//2),True,(0,0,0))
        screen.blit(text,(i,height//2+5))
    for j in range(0,height,100):
        text = font.render(str(height//2-j),True,(0,0,0))
        screen.blit(text,(width//2+5,j))
    # Draw circle
    pygame.draw.circle(screen,(255,0,0),(x,y),radius)
    # Show circle coordinates
    coord_text = font.render(f"Circle Position: X={x-width//2} Y={height//2-y}",True,(0,0,255))
    screen.blit(coord_text,(10,10))
    pygame.display.update()
    clock.tick(60)
