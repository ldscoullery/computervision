# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import cv2


"""En este módulo se leen las imagenes y se hacen las distintas conversiones
para los colores"""


imagen = cv2.imread('imagen-test.jpg')

print type(imagen)

print imagen.shape
# (8, 8, 3) ancho, alto, colores


# esto lo hacemos porque OpenCV (BGR) y Matplotlib (RGB)
imagen_ajuste_color = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

imagen_blanco_negro = cv2.imread('imagen-test.jpg', cv2.IMREAD_GRAYSCALE)

#plt.imshow(imagen_blanco_negro, cmap='gray')

fig = plt.figure()
ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)

ax1.imshow(imagen)
ax2.imshow(imagen_ajuste_color)
ax3.imshow(imagen_blanco_negro, cmap='gray')
#ax4.imshow(iar4)

plt.show()
