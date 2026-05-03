import pygame
import os

pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("2 tutorial")

stationary = pygame.image.load(os.path.join("Hero", "standing.png"))
left =  [pygame.image.load(os.path.join("Hero", "L1.png")),
         pygame.image.load(os.path.join("Hero", "L2.png")),
         pygame.image.load(os.path.join("Hero", "L3.png")),
         pygame.image.load(os.path.join("hero", "L4.png")),
         pygame.image.load(os.path.join("Hero", "L5.png")),
         pygame.image.load(os.path.join("Hero", "L6.png")),
         pygame.image.load(os.path.join("Hero", "L7.png")),
         pygame.image.load(os.path.join("hero", "L8.png")),
         pygame.image.load(os.path.join("Hero", "L9.png"))
        ]

right = [None]*10
for picIndex in range(1, 10):
    right[picIndex-1] = pygame.image.load(os.path.join("Hero", "R" + str(picIndex) + ".png"))
    picIndex+=1

x = 250
y = 250
vel = 10
move_left = False
move_right = False
stepIndex = 0

def draw_game():
    global stepIndex
    win.fill((0, 0, 0))
    if stepIndex >= 9:
        stepIndex = 0
    if move_left:
        win.blit(left[stepIndex], (x, y))
        stepIndex += 1
    elif move_right:
        win.blit(right[stepIndex], (x, y))
        stepIndex += 1
    else:
        win.blit(stationary, (x, y))

run = True
while run:

    draw_game()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    userInput = pygame.key.get_pressed()

    if userInput[pygame.K_LEFT] and x > 0:
        x -= vel
        move_left = True
        move_right = False
    elif userInput[pygame.K_RIGHT] and x < 500:
        x += vel
        move_left = False
        move_right = True
    else:
        move_left = False
        move_right = False
        stepIndex = 0

    pygame.time.delay(30)

    pygame.display.update()