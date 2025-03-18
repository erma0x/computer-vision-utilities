descrizione = """
Il codice Python presentato utilizza la libreria OpenCV, una delle più popolari per l'elaborazione delle immagini. 
Inizialmente, viene definito il percorso dell'immagine da caricare, specificando un file JPEG situato nella cartella 
"img-test". La funzione cv2.imread() viene quindi utilizzata per leggere l'immagine, 
con il secondo argomento impostato a 0, il che indica che l'immagine deve essere caricata in scala di grigi.
Il risultato della lettura dell'immagine è memorizzato nella variabile img. Infine, 
il programma stampa il contenuto della variabile img, che rappresenta una matrice bidimensionale contenente 
i valori dei pixel dell'immagine in scala di grigi. Questo codice è un ottimo punto di partenza per chi desidera esplorare ulteriormente le funzionalità di OpenCV, come la manipolazione e l'analisi delle immagini.
"""

import cv2  # Importa la libreria OpenCV, necessaria per la manipolazione delle immagini.

path_immagine_documento = ".\documents\id1.jpg"  # Definisce il percorso dell'immagine da caricare.

img = cv2.imread(path_immagine_documento, 0)  # Carica l'immagine specificata nel percorso in scala di grigi (0 indica scala di grigi).

print(img)  # Stampa i dati dell'immagine caricata, che saranno una matrice di pixel.
