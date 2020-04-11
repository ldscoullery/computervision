# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import cv2


""" MANIPULACION DE IMAGENES """

imagen = cv2.imread('imagen-test.jpg')

plt.imshow(imagen)
plt.show()

imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

plt.imshow(imagen)
plt.show()


print imagen.shape

# le queremos cambiar el tamaño
imagen2 = cv2.resize(imagen, (600, 500)) # ancho y alto

plt.imshow(imagen2)
plt.show()

# tambien podemos modificarle un % 
ratio_ancho = 0.5
ratio_alto = 0.5

imagen2 = cv2.resize(imagen2, (0,0), imagen2, ratio_ancho, ratio_alto)

plt.imshow(imagen2)
plt.show()

# podemos invertir la imagen
imagen2 = cv2.flip(imagen2, 1) # 1 lo espeja y 0 lo da vuelta de arriba a abajo

imagen2 = cv2.flip(imagen2, 0)
# si quisiera guardar la imagen
imagen2 = cv2.cvtColor(imagen2, cv2.COLOR_RGB2BGR)
cv2.imwrite('imagen-test-al-reves.jpg', imagen2)