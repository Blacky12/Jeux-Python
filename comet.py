import pygame
import random

# Creer une classe pour gérer cette comete
class Comet(pygame.sprite.Sprite):

     def __init__(self,comet_event):
         super().__init__()
         # Définir l'image accocié à cette commette
         self.image = pygame.image.load('assets/comet.png')
         self.rect = self.image.get_rect()
         self.velocity = random.randint(1, 3)
         self.rect.x = random.randint(20,800)
         self.rect.y = - random.randint(0, 800)
         self.comet_event = comet_event

     def remove(self):
        self.comet_event.all_comets.remove(self)
        # jouer le son
        self.comet_event.game.sound_manager.play('meteorite')
        
        # Verifier si le nombre de comettes est de 0
        if len(self.comet_event.all_comets)== 0:
            print("L'évenement est fini")
            #Rettre la barre à 0
            self.comet_event.reset_percent()
            # Apparaitre les 2 premier monstre
            self.comet_event.game.start()


     def fall(self):
         self.rect.y += self.velocity


         # Ne tombe pas sur le sol
         if self.rect.y >= 500 :
             print("sol")
             # Retirer la boule de feu
             self.remove()

             # Si il n'y plus de boule de feu
             if len(self.comet_event.all_comets) == 0:
                 print("L'évenement est fini")
                 # Remettre la jauge au départ
                 self.comet_event.reset_percent()
                 self.comet_event.fall_mod = False
        
        # Verifier si la boule de feu touche le jouer
         if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
             print("Joueur toucher")
             # Retirer la boule de feu
             self.remove()
             # Subir 20 points de dégats
             self.comet_event.game.player.damage(20)