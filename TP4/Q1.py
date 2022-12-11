import os
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

#Lecture de l'image
coco = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\Images\\coco.bmp"
I = plt.imread(coco)

def dilatation(image, se):
    # Initialisation de la sortie
    output = np.zeros(image.shape, dtype=np.uint8)
    # On explore chaque pixel de l'image
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            # On parcourt chaque élément du masque
            for k in range(se.shape[0]):
                for l in range(se.shape[1]):
                    # Si le pixel est à 1 dans le masque
                    if se[k, l] == 1:
                        # On applique la dilatation
                        if image[i-k, j-l] == 1:
                            output[i, j] = 1
    return output

    
def erosion(image, kernel):
 output = np.zeros_like(image)
 image_padded = np.zeros((image.shape[0] + 2, image.shape[1] + 2))
 image_padded[1:-1, 1:-1] = image
 for x in range(image.shape[1]):
    for y in range(image.shape[0]):
        output[y,x]=(kernel*image_padded[y:y+3,x:x+3]).min()
    return output

