#Ecrire sous Python la fonction de convolution Convol(I,Mask) ou utiliser 
#la fonction intégrée signal.convolve2d(I, Mask) de la librairie scipy de Python.
#Interprétation des résultats de l'opérateur de renforcement de contraste. 

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#Lecture de l'image
coco = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\Images\\coco.bmp"
I = plt.imread(coco)

#Masque de convolution de renforcement de contraste
Mask = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])

#Convolution de l'image par le masque 1 fois
M = signal.convolve2d(I, Mask, boundary='symm', mode='same')

#Convolution de l'image par le masque 2 fois
J = signal.convolve2d(M, Mask, boundary='symm', mode='same')

#Affichage
plt.figure()
plt.imshow(I, cmap='gray')
plt.title('Image originale')
plt.figure()
plt.imshow(M, cmap='gray')
plt.title('Image à contraste renforce')
plt.figure()
plt.imshow(J, cmap='gray')
plt.title('Image à contraste renforce 2 fois')
plt.show()