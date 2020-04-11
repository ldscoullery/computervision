import cv2
import numpy as np

cam = cv2.VideoCapture(0)

kernel = np.ones((5,5), np.uint8) #valores de 8 bits

while True:
    #ret detecta si se reciben imagenes (true o false) y frame detecta
    # la imagen en milisec
    ret,frame = cam.read() 
    #vamos a detectar un objeto verde
    rangomax = np.array([50, 255, 50])
    rangomin = np.array([0, 51, 0])
    # cuando un pixel se encuentre dentro del rango va a ser un punto blanco y sino negro
    mascara = cv2.inRange(frame, rangomin, rangomax)
    # eliminamos ruido
    opening = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
    #dibujamos el rectangulo
    x,y,w,h = cv2.boundingRect(opening)
    cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 0), 3)
    #queremos dibujar el centro del rectangulo
    cv2.circle(frame, (x+w/2, y+h/2), 5, (0,0,255), -1)
    cv2.imshow('camara', frame)
    
    # para cerrar la ventana
    k = cv2.waitKey(1) & 0xFF
    
    if k == 27:
        break
    