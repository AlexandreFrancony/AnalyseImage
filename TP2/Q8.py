#Ecrire sous Python la fonction de débruitage basée sur la Transformée de Fourier (TF) 
#(fonctions numpy.fft.fft(s) (TF) et numpy.fft.ifft(S) (TF inverse) de la librairie numpy de Python). 
#Tester sur l'image "kit256noisy.bmp". Interprétation des résultats.

import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#Lecture de l'image
kit = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\Images\\kit256noisy.bmp"
I = plt.imread(kit)

#Fonction de débruitage
def Debruitage(I):
    #TF de l'image
    S = np.fft.fft2(I)
    #Filtrage
    S = np.where(np.abs(S) < 10, 0, S)
    #TF inverse
    S = np.fft.ifft2(S)
    return S

#Débruitage
D = Debruitage(I)

#Affichage
plt.figure()
plt.imshow(I, cmap='gray')
plt.title('Image originale')
plt.figure()
plt.imshow(D, cmap='gray')
plt.title('Image débruitée')
plt.show()