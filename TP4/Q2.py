#Transposer sous Python l'algorithme d'axe median. Test sur autres images binaires

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage

#Lecture de l'image
coco = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\Images\\coco.bmp"
img = plt.imread(coco)

#Affichage de l'image
plt.imshow(img, cmap='gray')
plt.show()

#Calcul de l'axe median
def median_axis(img):
    #Calcul de la distance de chaque pixel à l'origine
    dist = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            dist[i,j] = np.sqrt(i**2+j**2)
    #Calcul de l'axe median
    axis = np.zeros(img.shape)
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            if img[i,j] == 1:
                axis[i,j] = dist[i,j]
    return axis

#Calcul de l'axe median
axis = median_axis(img)

#Affichage de l'axe median
plt.imshow(axis, cmap='gray')
plt.show()