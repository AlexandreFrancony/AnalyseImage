#Ecrire sous Python la fonction de convolution Convol(I,Mask) ou utiliser 
#la fonction intégrée signal.convolve2d(I, Mask) de la librairie scipy de Python.
#Interprétation des résultats de l'opérateur de renforcement de contraste. 

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#Lecture de l'image
I = plt.imread('images/coco.bmp')

#Masque de convolution
Mask = np.array([[0,0,0],[0,1,0],[0,0,0]])

#Convolution
I2 = signal.convolve2d(I, Mask, boundary='symm', mode='same')

#Affichage
plt.figure()
plt.imshow(I, cmap='gray')
plt.title('Image originale')
plt.figure()
plt.imshow(I2, cmap='gray')
plt.title('Image convoluee')
plt.show()