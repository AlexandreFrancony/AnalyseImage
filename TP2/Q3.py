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
def Chanda(I,n):


#J'ai rien compris à l'algorithme de Chanda, je ne sais pas comment coder ça.