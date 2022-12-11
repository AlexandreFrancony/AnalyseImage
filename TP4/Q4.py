# Importation des bibliothèques nécessaires
import numpy as np 
import cv2 

# Fonction pour dilater l'image
def dilatation(image, kernel):
    """
    Cette fonction applique une dilatation sur l'image de luminance donnée
    en utilisant un noyau spécifié.

    Arguments:
    image -- L'image de luminance à traiter
    kernel -- Le noyau à utiliser pour appliquer la dilatation

    Retourne:
    dilated_image -- L'image dilatée
    """
    # Applique la dilatation
    dilated_image = cv2.dilate(image, kernel)

    return dilated_image

# Fonction pour éroder l'image
def erosion(image, kernel):
    """
    Cette fonction applique une érosion sur l'image de luminance donnée
    en utilisant un noyau spécifié.

    Arguments:
    image -- L'image de luminance à traiter
    kernel -- Le noyau à utiliser pour appliquer l'érosion

    Retourne:
    eroded_image -- L'image érodée
    """
    # Applique l'érosion
    eroded_image = cv2.erode(image, kernel)

    return eroded_image