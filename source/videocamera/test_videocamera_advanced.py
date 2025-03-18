"""
Questo codice rappresenta un esempio pratico di acquisizione e manipolazione di immagini in tempo reale utilizzando OpenCV.
La combinazione di maschere e immagini in scala di grigi offre un modo creativo per visualizzare i dati acquisiti dalla fotocamera.

"""

import time
import cv2
import numpy as np
from settings.settings import CAMERA

camera_index = 0  # Indice della fotocamera
cam = cv2.VideoCapture(camera_index)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA['width'])
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA['height'])

print("Guarda la fotocamera e aspetta...")

cv2.startWindowThread()
titolo_finestra = "Acquisizione facciale con AI"
cv2.namedWindow(titolo_finestra)

while True:
    
    ret, img = cam.read()

    if ret:

        # Convertire l'immagine in scala di grigi
        gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        # Creare un'immagine a colori per la maschera
        img_colored = img.copy()

        # Definire il centro dell'ellisse
        center_coordinates = (int(CAMERA['width'] / 2), int(CAMERA['height'] / 2))  # Centro dell'immagine
        axes_length = (100, 135)  # Lunghezza degli assi dell'ellisse (maggiore, minore)
        angle = 0  # Angolo di rotazione dell'ellisse
        color = (0, 0, 255)  # Colore dell'ellisse in BGR (Blu, Verde, Rosso)
        thickness = -1  # Riempire l'ellisse

        # Creare una maschera nera
        mask = np.zeros_like(img)

        # Disegnare l'ellisse sulla maschera
        cv2.ellipse(mask, center_coordinates, axes_length, angle, 0, 360, (255, 255, 255), thickness)

        # Applicare la maschera all'immagine a colori
        masked_img = cv2.bitwise_and(img_colored, mask)

        # Convertire l'immagine in scala di grigi
        gray_img_colored = cv2.cvtColor(gray_img, cv2.COLOR_GRAY2BGR)
        # Combinare l'immagine grigia con l'immagine mascherata
        final_img = cv2.addWeighted(gray_img_colored, 0.7, masked_img, 1, 0)

        # Mostrare l'immagine finale
        cv2.imshow(titolo_finestra, final_img)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Premi 'q' per uscire
        break

cam.release()
cv2.destroyAllWindows()
