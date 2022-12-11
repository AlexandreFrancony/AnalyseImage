# Compléter l'algorithme zoomCart pour réaliser un zoom en coordonnées cartésiennes
import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from math import *

#Lecture de l'image
image = plt.imread(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\Images\\coco.bmp")

#algorithme de zoom en coordonnées cartésiennes
def ZoomCart(image, zoom):
    #initialisation
    h, w = image.shape
    h2 = int(h/2)
    w2 = int(w/2)
    image2 = np.zeros((h, w), dtype=np.uint8)
    #zoom de l'image en coordonnées cartésiennes
    for i in range(h):
        for j in range(w):
            x = int((i-h2)/zoom+h2)
            y = int((j-w2)/zoom+w2)
            if x>=0 and x<h and y>=0 and y<w:
                image2[i, j] = image[x, y]
    return image2

#affectation de la fonction ZoomCart à la variable image2 en coordonnées cartésiennes
image2 = ZoomCart(image, 0.7)

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



