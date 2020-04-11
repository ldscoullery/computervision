# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import cv2


""" DIBUJAR FIGURAS EN IMAGENES (rectangulo, circulo, linea) """

# creamos imagen en color negro
imagen = np.zeros(shape=[500,500,3], dtype=np.int16)

print imagen.shape

# sobre esta imagen negro vamos a pintar un cuadrado de color rojo
# pt1=punto 1 de donde arranca
# pt2=punto 2 de donde termina
# color en rgb rojo
# thickness el grosor
cv2.rectangle(imagen, pt1=(20,20), pt2=(100,100), color=(255,0,0), thickness=10)

# para dibujar un circulo verde
cv2.circle(imagen, center=(250,250), radius=100, color=(0,255,0), thickness=10)

# para dibujar una recta azul
cv2.line(imagen, pt1=(0,400), pt2=(500,400), color=(0,0,255), thickness=10)

plt.imshow(imagen)
plt.show()