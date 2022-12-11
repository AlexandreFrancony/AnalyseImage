# Q1.2. Proposer une solution pour améliorer l'algorithme de Rotation en coordonnées cartésiennes (disparition des points noirs).
# Expliquer la méthode, la coder sous Python, la tester sur différentes images, consigner les résultats (copies d'écran) et les interpréter (limites éventuelles de la méthode, autres améliorations ...)

import os
import numpy as np
import matplotlib.pyplot as plt
import math as m

def RotationCartesienne(image, angle):
    # Initialisation
    angle = m.radians(angle)
    cos = m.cos(angle)
    sin = m.sin(angle)
    h, w = image.shape
    h2 = int(h/2)
    w2 = int(w/2)
    image2 = np.zeros((h, w), dtype=np.uint8)

    # Rotation de l'image avec disparition des points noirs
    for i in range(h):
        for j in range(w):
            x = int((j-w2)*cos - (i-h2)*sin + w2)
            y = int((j-w2)*sin + (i-h2)*cos + h2)
            if x >= 0 and x < w and y >= 0 and y < h:
                image2[i, j] = image[y, x]
    return image2

# Programme principal
if __name__ == '__main__':
    # Lecture de l'image
    image = plt.imread(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\Images\\coco.bmp")

    # Affichage de l'image
    plt.figure()
    plt.imshow(image, cmap='gray')
    plt.title('Image originale')
    plt.axis('off')

    # Rotation de l'image
    image2 = RotationCartesienne(image, 45)

    # Affichage de l'image transformée
    plt.figure()
    plt.imshow(image2, cmap='gray')
    plt.title('Image transformée')
    plt.axis('off')

    # Affichage des images
    plt.show()