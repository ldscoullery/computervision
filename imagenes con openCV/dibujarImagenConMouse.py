# -*- coding: utf-8 -*-
import numpy as np
import cv2


""" DIBUJAR CON EL MOUSE UN CIRCULO SOBRE LA IMAGEN HACIENDO CLICK """

# Definimos la funcion para dibujar con el mouse
def dibujar(event, x, y, etiquetas, parametros):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(imagen, (x,y), 50, (255,0,0), -1) # -1 circulo relleno
        

# Conectamos la imagen con la funcion dibujar

cv2.namedWindow(winname='mi_imagen') # ojo que coincida el nombre con el de la imagen creada
cv2.setMouseCallback('mi_imagen', dibujar) # ojo que coincida el nombre con el nombre de abajo


# Mostramos la imagen donde vamos a pintar

imagen = np.zeros((500,500,3), np.int8)

while True:
    
    cv2.imshow('mi_imagen', imagen)
    
    # salgo cuando presiono Esc
    if cv2.waitKey(10) & 0XFF == 27:
        break

cv2.destroyAllWindows()
