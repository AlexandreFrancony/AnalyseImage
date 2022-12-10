#Programmer l'opérateur de lissage median 3x3. Interprétation des résultats.

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#Lecture de l'image
cube = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\Images\\cube.bmp"
I = plt.imread(cube)

#Fonction Median(I,Mask3x3)
def Median(I,Mask3x3):
    return signal.convolve2d(I, Mask3x3, boundary='symm', mode='same')
    
#Masque 3x3
Mask3x3 = np.ones((3,3))/9

#Application de l'opérateur de lissage median 3x3
J = Median(I,Mask3x3)

#Affichage des images
plt.figure()
plt.subplot(1,2,1)
plt.imshow(I,cmap='gray')
plt.title('Image originale')
plt.axis('off')
plt.subplot(1,2,2)
plt.imshow(J,cmap='gray')
plt.title('Image filtrée')
plt.axis('off')
plt.show()

#Interprétation des résultats
#L'opérateur de lissage median 3x3 est un filtre non linéaire. Il est donc
#plus adapté pour supprimer le bruit impulsionnel que le bruit gaussien.