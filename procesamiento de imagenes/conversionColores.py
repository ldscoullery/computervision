import cv2
import numpy as np
import matplotlib.pyplot as plt

""" CONVERSION ENTRE COLORES """

# ABRIMOS IMAGEN ORIGINAL
imagen = cv2.imread('../imagenes-test/imagen-test.jpg')

# CONVERTIMOS BGR A RGB
imagen_ajuste_color = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)

# CONVERTIMOS A COLOR HSV
imagen_ajuste_hsv = cv2.cvtColor(imagen, cv2.COLOR_BGR2HSV)

# CONVERTIMOS A COLOR HSL
imagen_ajuste_hsl = cv2.cvtColor(imagen, cv2.COLOR_BGR2HLS)


# dibujamos todas las figuras
fig = plt.figure()
ax1 = plt.subplot2grid((8,6), (0,0), rowspan=4, colspan=3)
ax2 = plt.subplot2grid((8,6), (4,0), rowspan=4, colspan=3)
ax3 = plt.subplot2grid((8,6), (0,3), rowspan=4, colspan=3)
ax4 = plt.subplot2grid((8,6), (4,3), rowspan=4, colspan=3)

ax1.imshow(imagen)
ax2.imshow(imagen_ajuste_color)
ax3.imshow(imagen_ajuste_hsv)
ax4.imshow(imagen_ajuste_hsl)

plt.show()