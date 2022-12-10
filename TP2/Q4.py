import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#Lecture de l'image
cube = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\Images\\cube.bmp"
I = plt.imread(cube)

#Fonction Derivation(I,Mask3x3)
def Derivation(I,Mask3x3):
    return signal.convolve2d(I, Mask3x3, boundary='symm', mode='same')

#Masque de convolution de dérivation
Mask = np.array([[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]])

#Convolution de l'image par le masque 1 fois
D = Derivation(I, Mask)

#Affichage
plt.figure()
plt.imshow(I, cmap='gray')
plt.title('Image originale')
plt.figure()
plt.imshow(D, cmap='gray')
plt.title('Image lissée')
plt.show()