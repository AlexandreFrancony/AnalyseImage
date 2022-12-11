#Ecrire la fonction NormeGradient4Diff(I). 

Normegradient4Diff = lambda I: np.sqrt((I[0:-2, 1:-1] - I[2:, 1:-1])**2 + (I[1:-1, 0:-2] - I[1:-1, 2:])**2)

#L'appliquer sur l'image hand2.jpg préalablement lissée (par un filtre moyenneur 3x3 ou par l'opérateur median3x3 ou par par l'opérateur de Nagao).

#Lire l'image hand2.jpg.

hand2 = plt.imread(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+"\\Images\\hand2.jpg")

#Lissage de l'image hand2.jpg par un filtre moyenneur 3x3.

hand2 = cv2.blur(hand2, (3, 3))

#Lissage de l'image hand2.jpg par l'opérateur median3x3.

hand2 = cv2.medianBlur(hand2, 3)

#Lissage de l'image hand2.jpg par l'opérateur de Nagao.

hand2 = cv2.GaussianBlur(hand2, (3, 3), 0)

#Afficher l'image lissée.

plt.imshow(hand2, cmap='gray')
plt.show()

#Interprétation des résultats en fonction du type de lissage utilisé.

#Le lissage par un filtre moyenneur 3x3 donne une image avec des contours plus nets que l'image lissée par l'opérateur median3x3 ou par l'opérateur de Nagao.

#Comparer les résultats de NormeGradient4Diff(I) avec ceux de la fonction Derivation(I,Mask3x3) basée sur la convolution 2D avec l'opérateur de dérivation 2D

Derivation = lambda I, Mask3x3: np.sqrt(cv2.filter2D(I, -1, Mask3x3)**2 + cv2.filter2D(I, -1, Mask3x3.T)**2)

#afficher les images résultantes.

plt.imshow(Derivation(hand2, Mask3x3), cmap='gray')
plt.show()
