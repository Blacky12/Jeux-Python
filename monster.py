import pygame
import random

# Creez une classe qui va géré la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100   
        self.max_health = 100
        self.attack = 0.3
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0,300)
        self.rect.y = 540
        self.velocity = random.randint(1, 3)

    def damage(self, amount):
        # Inflige des dégats
        self.health -= amount
        # Verifier si son nouveau nombre de point de vie est initialiser
        if self.health <= 0:
            # Réaparaitre comme un nouveau monstre
            self.rect.x = 1000 + random.randint(0,300)
            self.velocity = random.randint(1, 3)
            self.health = self.max_health

    
    def update_healht_bar(self,surface):

        # Dessiner notre barre de vie
        pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 20, self.max_health ,5])
        pygame.draw.rect(surface, (111,210,46) , [self.rect.x + 10, self.rect.y - 20, self.health ,5])


    def forward(self):
        # le déplacement ne se fait que si il n'y a pas de collision avec le joueur avec un groupe de joueur
        if not self.game.check_collision(self ,self.game.all_players):
            self.rect.x -= self.velocity
        # si le monstre est en collision
        else:
            self.game.player.damage(self.attack)

        
