import pygame
pygame.init()

# Générer la fenêtre de notre jeux

pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080,720))


# Importer de charger l'arrière plan de notre jeux 
background = pygame.image.load("assets/bg.jpg")



running = True

# Boucle tant que cette condition est vrai

while running:

    # Appliquer l'arrière plan
    screen.blit(background, (0,-200))

    # mettre à jour notre écran
    pygame.display.flip()

    # Si le joueur ferme cette fenêtre


    for event in pygame.event.get():
        # Que l'evenement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeux")
