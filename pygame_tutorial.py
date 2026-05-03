import pygame

pygame.init()
ORANGE  = ( 255, 140, 0)
ROT     = ( 255, 0, 0)
GRUEN   = ( 0, 255, 0)
SCHWARZ = ( 0, 0, 0)
WEISS   = ( 255, 255, 255)

screen = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()
pygame.display.set_caption(("Test game"))
spielaktiv = True
while spielaktiv:
    # Überprüfen, ob Nutzer eine Aktion durchgeführt hat
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            spielaktiv = False
            print("Spieler hat Quit-Button angeklickt")
        elif event.type == pygame.KEYDOWN:
            print("Spieler hat Taste gedrückt")

            # Taste für Spieler 1
            if event.key == pygame.K_RIGHT:
                print("Spieler hat Pfeiltaste rechts gedrückt")
            elif event.key == pygame.K_LEFT:
                print("Spieler hat Pfeiltaste links gedrückt")
            elif event.key == pygame.K_UP:
                print("Spieler hat Pfeiltaste hoch gedrückt")
            elif event.key == pygame.K_DOWN:
                print("Spieler hat Pfeiltaste runter gedrückt")
            elif event.key == pygame.K_SPACE:
                print("Spieler hat Leertaste gedrückt")

            # Taste für Spieler 2
            elif event.key == pygame.K_w:
                print("Spieler hat Taste w gedrückt")
            elif event.key == pygame.K_a:
                print("Spieler hat Taste a gedrückt")
            elif event.key == pygame.K_s:
                print("Spieler hat Taste s gedrückt")
            elif event.key == pygame.K_d:
                print("Spieler hat Taste d gedrückt")

        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Spieler hast Maus angeklickt")
    
    screen.fill(GRUEN)
    
    pygame.display.flip()

    clock.tick(60)