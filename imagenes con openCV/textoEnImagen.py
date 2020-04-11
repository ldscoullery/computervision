# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import cv2


""" TEXTO EN IMAGENES + POLIGONO (util para cuando detectemos rostro en imagen) """

# creamos imagen en color negro
imagen = np.zeros(shape=[500,500,3], dtype=np.int16)

print imagen.shape

# Definimos tipo de fuente
fuente = cv2.FONT_HERSHEY_SCRIPT_COMPLEX

# creamos el texto en verde
cv2.putText(imagen, text='Hola', org=(20,100), fontFace=fuente, fontScale=3,
    color=(0,255,0), thickness=4, lineType=cv2.LINE_8)

# Ahora vamos a dibujar un poligono en la imagen
vertices = np.array([ [100,300], [300,200], [400,400], [200,400] ], dtype=np.int32)

print vertices.shape

# tenemos que hacerle un reshape por las 3 dimensiones
puntos = vertices.reshape(-1,1,2)

print puntos.shape

cv2.polylines(imagen, [puntos], isClosed=True, color=(255,255,255), thickness=5)

# nota: con los vertices me funcionó también, habría que ver que diferencia hay real

plt.imshow(imagen)
plt.show()