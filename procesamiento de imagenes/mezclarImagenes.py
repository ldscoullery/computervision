import cv2
import numpy as np
import matplotlib.pyplot as plt

""" MEZCLAR 2 IMAGENES llevandolas al mismo tamanio """
'''
# ABRIMOS IMAGEN ORIGINAL
imagen_1 = cv2.imread('../imagenes-test/perro.jpg')

# CONVERTIMOS BGR A RGB
imagen_1 = cv2.cvtColor(imagen_1, cv2.COLOR_BGR2RGB)

plt.imshow(imagen_1)
plt.show()

imagen_2 = cv2.imread('../imagenes-test/marca-de-agua.jpg')

imagen_2 = cv2.cvtColor(imagen_2, cv2.COLOR_BGR2RGB)

plt.imshow(imagen_2)
plt.show()

# cambiamos tamanio a ambas imagenes
imagen_1 = cv2.resize(imagen_1, (1200, 1200))
imagen_2 = cv2.resize(imagen_2, (1200, 1200))

plt.imshow(imagen_2)
plt.show()

# Funcion que mezcla ambas imagenes
imagen_mezcla = cv2.addWeighted(src1=imagen_1, alpha=0.5, src2=imagen_2, beta=0.5, gamma=0)

plt.imshow(imagen_mezcla)
plt.show()
'''
# ---------------------------------------------------------------------------

""" MEZCLAR 2 IMAGENES de distinto tamanio """

imagen_1 = cv2.imread('../imagenes-test/perro.jpg')
imagen_1 = cv2.cvtColor(imagen_1, cv2.COLOR_BGR2RGB)

print imagen_1.shape

plt.imshow(imagen_1)
plt.show()

imagen_2 = cv2.imread('../imagenes-test/marca-de-agua.jpg')
imagen_2 = cv2.cvtColor(imagen_2, cv2.COLOR_BGR2RGB)

plt.imshow(imagen_2)
plt.show()

# hacemos resize de la imagen 2 (Ver shape imagen 1, solo queremos 300px)
imagen_2 = cv2.resize(imagen_2, (1920, 300))

plt.imshow(imagen_2)
plt.show()

# extraemos solo los 300 px de la imagen 1
parte_imagen_1 = imagen_1[:300]
plt.imshow(parte_imagen_1)
plt.show()

# Funcion que mezcla ambas imagenes
parte_imagen_mezcla = cv2.addWeighted(src1=parte_imagen_1, alpha=0.5, src2=imagen_2, beta=0.5, gamma=0)

plt.imshow(parte_imagen_mezcla)
plt.show()


#sustituimos en la imagen1 la parte de imagen creada
imagen_1[:300] = parte_imagen_mezcla

plt.imshow(imagen_1)
plt.show()




