import pygame

# Defenir une classe qui va s'occuper des animations

class AnimateSprite(pygame.sprite.Sprite):

    # Defenir les choses à faire à la création de l'entité
    def __init__(self, sprite_name, size=(200,200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image,size)
        self.current_image = 0 # Pour dire de commencer l'animation à l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    
    # Definir une methode pour démarrer l'animation
    def start_animation(self):
        self.animation = True

    # definir une méthode pour animer le sprite
    def animate(self,loop = False):
        
        # Verifier si l'animation est active
        if self.animation:

            # Passer à l'image suivante
            self.current_image += 1

            # Verifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                # remettre l'animation au départ
                self.current_image = 0

                # Verifier si l'animation n'est pas en mode boucle
                if loop is False:
                     # Désactivation de l'animation
                    self.animation = False


            # Modifier l'image de l'animation précédente par la suivante
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image,self.size)

# Definir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    # Charger les 24 images de ce sprite dans le dossier correspondant
    images = []
    # Recupérerle chemin du dossier pour ce sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    # Boucler sur chaque image dans ce dossier à la liste
    for num in range(1,24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

    # Renvoyer le contenu de la liste d'images
    return images


# Definir un dictionnaire qui va contenir les images chargées de chaque sprite
# Besoin qql qui regroupe exemple un dictionnaire qui permet d'associer des clefs et des valeurs mummy -> [... mummy2.png, ...] (Si on veux récupérer
# tout le contenue il suffit juste faire reference à la clef mummy)
# player -> [...player1.png,...player2.png,..]
animations = {
    'mummy': load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien':load_animation_images('alien')
}
