import pygame
import os
pygame.init()
win_height = 400
win_width = 800
win = pygame.display.set_mode((win_width, win_height))

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
right =  [pygame.image.load(os.path.join("Hero", "R1.png")),
         pygame.image.load(os.path.join("Hero", "R2.png")),
         pygame.image.load(os.path.join("Hero", "R3.png")),
         pygame.image.load(os.path.join("hero", "R4.png")),
         pygame.image.load(os.path.join("Hero", "R5.png")),
         pygame.image.load(os.path.join("Hero", "R6.png")),
         pygame.image.load(os.path.join("Hero", "R7.png")),
         pygame.image.load(os.path.join("hero", "R8.png")),
         pygame.image.load(os.path.join("Hero", "R9.png"))
        ]

background = pygame.transform.scale(pygame.image.load("background.png"), (win_width, win_height))

class Hero:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velx = 10
        self.vely = 10
        self.face_right = True
        self.face_left = False
        self.stepIndex = 0
        self.jump = False
        
    def move_hero(self, userInput):
        if userInput[pygame.K_RIGHT] and self.x <= win_width - 62:
            self.x += self.velx
            self.face_right =True
            self.face_left = False
        elif userInput[pygame.K_LEFT] and self.x >= 0:
            self.x -= self.velx
            self.face_right =False
            self.face_left = True
        else:
            self.stepIndex = 0
    def draw(self, win):
        if self.stepIndex >= 9:
            self.stepIndex = 0
        if self.face_left:
            win.blit(left[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
        if self.face_right:
            win.blit(right[self.stepIndex], (self.x, self.y))
            self.stepIndex += 1
    def jump_motion(self, userInput):
        if userInput[pygame.K_SPACE] and self.jump is False:
            self.jump = True
        if self.jump:
            self.y -= self.vely*4
            self.vely -= 1
        if self.vely < -10:
            self.jump = False
            self.vely = 10

def draw_game():
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))
    player.draw(win)
    pygame.time.delay(30)
    pygame.display.update()

player = Hero(250, 290)

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    userInput = pygame.key.get_pressed()

    player.move_hero(userInput)
    player.jump_motion(userInput)

    draw_game()