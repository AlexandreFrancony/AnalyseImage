#Coder sous Python l'algorithme de recadrage de dynamique d'une image.

# Path: AnalyseImage\TP1\Q7.py

import os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

#Lecture de l'image
image = plt.imread(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\Images\\coco.bmp")

#algorithme de recadrage de dynamique d'une image
def RecadrageDynamique(image):
    # Initialisation
    h, w = image.shape
    image2 = np.zeros((h, w), dtype=np.uint8)
    min = 255
    max = 0

    # Recherche du minimum et du maximum
    for i in range(h):
        for j in range(w):
            if image[i, j] < min:
                min = image[i, j]
            if image[i, j] > max:
                max = image[i, j]

    # Recadrage de dynamique
    for i in range(h):
        for j in range(w):
            image2[i, j] = int((image[i, j] - min) * 255 / (max - min))
    return image2

#Recadrage de dynamique de l'image
image2 = RecadrageDynamique(image)

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