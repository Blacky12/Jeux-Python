import pygame
pygame.init()

# Creez une seconde classe qui va representer notre jeux 
class Game:
    def __init__(self):
        # Generer notre joueur
        self.player = Player()
        

# Creez une premiere class qui va representer notre joueur
class Player(pygame.sprite.Sprite): 
    def __init__(self):
        super().__init__()
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 5
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500
    

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

    # mettre à jour notre écran
    pygame.display.flip()

    # Si le joueur ferme cette fenêtre


    for event in pygame.event.get():
        # Que l'evenement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Fermeture du jeux")
