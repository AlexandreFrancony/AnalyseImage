
def squelettisation(image):
 
    # Créer une copie de l'image
    img_copy = image.copy()
 
    # Définir les directions de voisinage
    directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
 
    # Répéter jusqu'à ce que la copie de l'image ne change pas
    while True:
 
        # Initialiser un booléen pour vérifier si l'image est modifiée
        is_modified = False
 
        # Parcourir tous les pixels de l'image
        for x in range(img_copy.shape[0]):
            for y in range(img_copy.shape[1]):
 
                # Vérifier si le pixel est un contour (valeur = 255)
                if img_copy[x, y] == 255:
 
                    # Initialiser un compteur pour compter le nombre de voisins contours
                    n_neighbours = 0
 
                    # Parcourir les directions de voisinage
                    for dx, dy in directions:
 
                        # Calculer les coordonnées du voisin
                        x_neighbour = x + dx
                        y_neighbour = y + dy
 
                        # Vérifier si le voisin est dans l'image
                        if 0 <= x_neighbour < img_copy.shape[0] and 0 <= y_neighbour < img_copy.shape[1]:
 
                            # Vérifier si le voisin est un contour
                            if img_copy[x_neighbour, y_neighbour] == 255:
                                n_neighbours += 1
 
                    # Vérifier si le nombre de voisins contour est inférieur à 2
                    if n_neighbours < 2:
 
                        # Remplacer le pixel par un fond (valeur = 0)
                        img_copy[x, y] = 0
 
                        # Modifier le booléen pour indiquer que l'image a été modifiée
                        is_modified = True
 
        # Vérifier si l'image a été modifiée
        if is_modified == False:
 
            # Sortir de la boucle
            break
 
    # Retourner la copie de l'image
    return img_copy