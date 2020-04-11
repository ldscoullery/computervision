import cv2
import numpy as np
import matplotlib.pyplot as plt

""" OPERADORES MORFOLOGICOS (efectos de erosion, eliminacion de ruido) """

# creamos cuadrado negro de 600x300
imagen = np.zeros((300,600))
print imagen.shape

fuente = cv2.FONT_HERSHEY_SIMPLEX
# creamos texto blanco
cv2.putText(imagen, text='ABCDE', org=(50,200), fontFace=fuente, fontScale=5,
    color=(255,255,255), thickness=8)
    
plt.imshow(imagen, cmap='gray')
plt.show()

# efecto de erosion - recortar las letras - funcion erode
nucleo = np.ones((5,5), dtype=np.uint8)
print nucleo

imagen_2 = cv2.erode(imagen, nucleo, iterations=1)
plt.imshow(imagen_2, cmap='gray')
plt.show()

# anadir ruido a la imagen
ruido = np.random.randint(low=0, high=2, size=(300,600))
print ruido[:1]
plt.imshow(ruido, cmap='gray')
plt.show()

ruido = ruido * 255
print ruido[:1]
imagen_ruido = imagen + ruido

plt.imshow(imagen_ruido, cmap='gray')
plt.show()

# recuperar la imagen de ruido
imagen_sin_ruido = cv2.morphologyEx(imagen, cv2.MORPH_OPEN, nucleo)
plt.imshow(imagen_sin_ruido, cmap='gray')
plt.show()

# de las letras intentar eliminar su relleno
gradiente = cv2.morphologyEx(imagen, cv2.MORPH_GRADIENT, nucleo)
plt.imshow(gradiente, cmap='gray')
plt.show()