#Coder sous Python l'algorithme de renforcement de contraste de Chanda et comparer ses résultats avec
#ceux de l'opérateur de renforcement de contraste basé sur la convolution.

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#Lecture de l'image
coco = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\Images\\coco.bmp"
I = plt.imread(coco)

#Fonction Chanda
def Chanda(I):
    return I - signal.convolve2d(I, Mask, boundary='symm', mode='same')

#Masque de convolution de dérivation
Mask = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

#Convolution de l'image par le masque 1 fois
D = Chanda(I)

#Affichage
plt.figure()
plt.imshow(I, cmap='gray')
plt.title('Image originale')
plt.figure()
plt.imshow(D, cmap='gray')
plt.title('Image dérivée')
plt.show()