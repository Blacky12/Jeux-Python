import pygame
import math # Importe le module math qui permet de faire plusieur calcul (arrondi,ect)
from game import Game
pygame.init()



# Générer la fenêtre de notre jeux

pygame.display.set_caption("Comet fall game")
screen = pygame.display.set_mode((1080,720))


# Importer de charger l'arrière plan de notre jeux 
background = pygame.image.load("assets/bg.jpg")

# Importer charger notre bannière (pygame.transform.scale(banner,(500,500)) --> Fonction qui permet de zommer ou dézoomer une image (image,dim))
banner = pygame.image.load('assets/banner.png')
banner = pygame.transform.scale(banner, (500,500))
banner_rect = banner.get_rect() # Fonction pour récupérer le rectangle associé à cette image
banner_rect.x = math.ceil(screen.get_width() / 4 ) # Screen represente la fenetetre et width pour récuper la largeur

# Importer charger notre bouton pour lancer la partie
play_button = pygame.image.load('assets/button.png')
play_button = pygame.transform.scale(play_button,(400,150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width() / 3.33 ) # La fonction get_width() permet de récupérer la hauteur
play_button_rect.y = math.ceil(screen.get_height() / 2) # La fonction get_height() permet de récupérer la hauteur
     
# Charger notre jeu
game = Game()


running = True

# Boucle tant que cette condition est vrai

while running:

    # Appliquer l'arrière plan
    screen.blit(background, (0,-200))

    # Verifier si notre jeu à commencé ou non
    if game.is_playing:
        # Déclencher les instruction de la partie
        game.update(screen)
    # Verifier si notre jeu n'a pas commencé
    else:
        # Ajouter mon ecran de bienvenue (screen.blit() --> Fonction qui permet d'injecter une image sur l'écran)
        screen.blit(play_button,play_button_rect)
        screen.blit(banner,banner_rect)
        

    # print(game.player.rect.x)


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

            # Detecter si la touche espace est enclenchée pour lancer notre projectile

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()


        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False


        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Verification pour savoir si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos): # Méthode collidepoint() --> Méthode qui permet de verifier si notre boutton correspond à notre souris au moment du clik
                # Mettre le jeu en mode "lancé"
                game.start()


