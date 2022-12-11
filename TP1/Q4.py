#Déduire de l'algorithme de rotation en coordonnées polaires, un algo. de zoom en coordonnées polaires

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import *

#Lecture de l'image
image = plt.imread(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\Images\\coco.bmp")

#algorithme de zoom en coordonnées polaires
def ZoomPolaires(image, zoom):
    # Initialisation
    h, w = image.shape
    h2 = int(h/2)
    w2 = int(w/2)
    image2 = np.zeros((h, w), dtype=np.uint8)

    # déZoom de l'image (agrandissement de l'image afin de voir plus de détails)
    for i in range(h):
        for j in range(w):
            x = int((j-w2)/zoom + w2)
            y = int((i-h2)/zoom + h2)
            if x >= 0 and x < w and y >= 0 and y < h:
                image2[i, j] = image[y, x]
    return image2

#Zoom de l'image
image2 = ZoomPolaires(image, 0.5)

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