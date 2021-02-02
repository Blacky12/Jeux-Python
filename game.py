import pygame
from player import Player
from monster import Monster

# Creez une seconde classe qui va representer notre jeux 
class Game:
    def __init__(self):
        # Definir si notre jeu à commencé ou non
        self.is_playing = False
        # Generer notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self) 
        self.all_players.add(self.player)
        # Creez un groupe de monstre
        self.all_monsters = pygame.sprite.Group()
        self.pressed = {}
    

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        # Remettre le jeu à neuf , retirer les monstre , remettre le joueur à 100 de vie , jeu en attente
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self,screen):
        # Appliquer l'image de mon joueur
        screen.blit(self.player.image , self.player.rect)

        # Appliquer la barre de vie de mon joueur
        self.player.update_healht_bar(screen)

        # Récupérer les porjectile du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # Récupérer les monstre de notre jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_healht_bar(screen)

        # Appliquer l'enssemble des image de mon groupe de projectile
        self.player.all_projectiles.draw(screen)

        # Appliquer l'enssemble des images de mon groupe de monstre
        self.all_monsters.draw(screen)

        # verifier si le joueur souhaite allez à gauche ou à droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_right()

        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x> 0:
            self.player.move_left()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite,group,False,pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster = Monster(self)
        self.all_monsters.add(monster)