def axe_median(image):
  # Créer une liste vide pour stocker les pixels
  pixels = []

  # Parcourir les lignes et les colonnes pour ajouter les pixels à la liste
  for ligne in range(image.shape[0]):
    for colonne in range(image.shape[1]):
      pixels.append(image[ligne, colonne])

  # Trier la liste
  pixels.sort()

  # Calculer l'axe médian
  median = len(pixels) // 2

  # Retourner l'axe médian
  return pixels[median]

# Appeler la fonction
axe_median(image)