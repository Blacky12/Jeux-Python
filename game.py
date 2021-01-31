import pygame
from player import Player

# Creez une seconde classe qui va representer notre jeux 
class Game:
    def __init__(self):
        # Generer notre joueur
        self.player = Player() 
        self.pressed = {}