import pygame
from game import Game
pygame.init()

   

# Générer la fenêtre de notre jeux

pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080,720))


# Importer de charger l'arrière plan de notre jeux 
background = pygame.image.load("assets/bg.jpg")

# Charger notre jeu
game = Game()


running = True

# Boucle tant que cette condition est vrai

while running:

    # Appliquer l'arrière plan
    screen.blit(background, (0,-200))

    # Appliquer l'image de mon joueur
    screen.blit(game.player.image , game.player.rect)

    # verifier si le joueur souhaite allez à gauche ou à droite
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()

    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x> 0:
        game.player.move_left()

    print(game.player.rect.x)


    # mettre à jour notre écran
    pygame.display.flip()

    # Si le joueur ferme cette fenêtre


    for event in pygame.event.get():
        # Que l'evenement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeux")
        # detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False
       
