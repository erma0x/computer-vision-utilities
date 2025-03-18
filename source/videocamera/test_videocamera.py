import cv2  # Importa la libreria OpenCV, fondamentale per la visione artificiale e l'elaborazione delle immagini.
from settings.settings import CAMERA  # Importa le impostazioni della telecamera da un modulo di configurazione.

camera_index = 0  # Definisce l'indice della telecamera da utilizzare. 0 di solito indica la telecamera predefinita.
cam = cv2.VideoCapture(camera_index)  # Inizializza l'oggetto VideoCapture per accedere alla telecamera specificata.
cam.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA['width'])  # Imposta la larghezza del frame della telecamera secondo le impostazioni.
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA['height'])  # Imposta l'altezza del frame della telecamera secondo le impostazioni.

print("Look at the camera and wait...")  # Stampa un messaggio per informare l'utente di posizionarsi davanti alla telecamera.
        
count = 0  # Inizializza un contatore, che potrebbe essere utilizzato per contare i frame o le immagini catturate.
cv2.startWindowThread()  # Avvia un thread per la gestione delle finestre di OpenCV, necessario per visualizzare le immagini.
cv2.namedWindow("preview")  # Crea una finestra chiamata "preview" per mostrare il video in tempo reale.

while True:  # Inizia un ciclo infinito per catturare e visualizzare i frame video.
    ret, img = cam.read()  # Legge un frame dalla telecamera. 'ret' è un valore booleano che indica se la lettura è riuscita, 'img' è l'immagine catturata.
    if ret:  # Controlla se il frame è stato catturato correttamente.
        cv2.imshow("preview", img)  # Mostra il frame catturato nella finestra "preview".
        
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Controlla se l'utente ha premuto il tasto 'q' per uscire dal ciclo.
        break  # Esce dal ciclo se il tasto 'q' è stato premuto.

cam.release()  # Rilascia la telecamera, liberando le risorse associate.
cv2.destroyAllWindows()  # Chiude tutte le finestre create da OpenCV.
