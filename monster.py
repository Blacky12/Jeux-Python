import pygame


# Creez une classe qui va géré la notion de monstre sur notre jeu
class Monster(pygame.sprite.Sprite):

    def __init__(self,game):
        super().__init__()
        self.game = game
        self.health = 100   
        self.max_health = 100
        self.attack = 5
        self.image = pygame.image.load('assets/mummy.png')
        self.rect = self.image.get_rect()
        self.rect.x = 1000
        self.rect.y = 540
        self.velocity = 2

    def forward(self):
        # le déplacement ne se fait que si il n'y a pas de collision avec le joueur avec un groupe de joueur
        if not self.game.check_collision(self ,self.game.all_players):
            self.rect.x -= self.velocity

        
