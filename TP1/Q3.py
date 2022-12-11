#Transposer sous Python l'algorithme de rotation en coordonnées polaires. 
#Pourquoi n'y-a-t-il pas de points noirs dans l'image issue de la rotation en coordonnées polaires ? 

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import *

#Lecture de l'image
image = plt.imread(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\Images\\coco.bmp")

#algoruthme de rotation en coordonnées polaires
def RotationPolaires(image, angle):
    # Initialisation
    angle = radians(angle)
    h, w = image.shape
    h2 = int(h/2)
    w2 = int(w/2)
    image2 = np.zeros((h, w), dtype=np.uint8)

    # Rotation de l'image avec disparition des points noirs
    for i in range(h):
        for j in range(w):
            x = int((j-w2)*cos(angle) - (i-h2)*sin(angle) + w2)
            y = int((j-w2)*sin(angle) + (i-h2)*cos(angle) + h2)
            if x >= 0 and x < w and y >= 0 and y < h:
                image2[i, j] = image[y, x]
    return image2

#Rotation de l'image
image2 = RotationPolaires(image, 45)


#Affichage de l'image de base
plt.figure()
plt.imshow(image, cmap='gray')
plt.title('Image originale')
plt.axis('off')

#Affichage de l'image transformée
plt.figure()
plt.imshow(image2, cmap='gray')
plt.title('Image transformée')
plt.axis('off')

#Affichage des images
plt.show()