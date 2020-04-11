import cv2
import numpy as np
import matplotlib.pyplot as plt

""" GRADIENTES Y CONTORNOS - METODO SOBEL Y LAPLACIAN """

# leemos la imagen en escala de grises
imagen = cv2.imread('../imagenes-test/sudoku.jpg', 0)

plt.imshow(imagen, cmap='gray')

plt.show()

# vamos a detectar contornos y nros - detecta las lineas verticales y nros
sobelx = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=5) # 1 detecta bbarra verticales y 0 barras horizontales
plt.imshow(sobelx, cmap='gray')
plt.show()

sobely = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=5) # 1 detecta bbarra verticales y 0 barras horizontales
plt.imshow(sobely, cmap='gray')
plt.show()

# ahora vamos a juntar las imagenes
imagen_2 = cv2.addWeighted(src1=sobelx, alpha=0.5, src2=sobely, beta=0.5, gamma=0)

plt.imshow(imagen_2, cmap='gray')
plt.show()

# ahora vamos a ver el otro metodo laplacian
# este en un solo paso detecta todo
laplacian = cv2.Laplacian(imagen, cv2.CV_64F)
plt.imshow(laplacian, cmap='gray')
plt.show()