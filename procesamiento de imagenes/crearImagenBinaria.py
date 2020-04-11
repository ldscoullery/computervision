import cv2
import matplotlib.pyplot as plt

""" CREAR IMAGEN EN BLANCO Y NEGRO - funcion threshold"""

# ABRIMOS IMAGEN ORIGINAL y la leemos en escala de grises
imagen = cv2.imread('../imagenes-test/perro.jpg', 0)

# vamos a convertir la imagen en imagen binaria blanco y negro
mitad, imagen_bin = cv2.threshold(imagen, 255/2, 255, cv2.THRESH_BINARY) #255/2=127 es para decidir si lo lleva a blanco o negro

mitad, imagen_bin_inv = cv2.threshold(imagen, 255/2, 255, cv2.THRESH_BINARY_INV) #blanco lo lleva a negro y negro a blanco

fig = plt.figure()
ax1 = plt.subplot2grid((2,2), (0,0), rowspan=1, colspan=1)
ax1.set_title('escala de grises')
ax2 = plt.subplot2grid((2,2), (1,0), rowspan=1, colspan=1)
ax2.set_title('imagen binaria')
ax3 = plt.subplot2grid((2,2), (0,1), rowspan=1, colspan=1)
ax3.set_title('imagen binaria inversa')
ax4 = plt.subplot2grid((2,2), (1,1), rowspan=1, colspan=1)
ax4.set_title('original bgr')


ax1.imshow(imagen, cmap='gray')
ax2.imshow(imagen_bin, cmap='gray')
ax3.imshow(imagen_bin_inv, cmap='gray')
ax4.imshow(imagen)

plt.show()

# Ahora si queremos que una imagen se muestre en grafico mas grande o mas chico
figura = plt.figure(figsize=(20,20))
lienzo = figura.add_subplot(111)
lienzo.imshow(imagen)
plt.show()