# Suppress macOS warning
import warnings
# Ignora i warning di tipo UserWarning
warnings.filterwarnings('ignore', category=UserWarning)

import json  # Importa il modulo per la gestione dei file JSON
import cv2  # Importa OpenCV per la manipolazione delle immagini
import os  # Importa il modulo per le operazioni sul sistema operativo
from typing import Optional, Dict  # Importa tipi opzionali e dizionari
import logging  # Importa il modulo per la registrazione dei log
from settings.settings import CAMERA, FACE_DETECTION, TRAINING, PATHS  # Importa le impostazioni da un modulo esterno

descrizione = """
Questo programma rappresenta un esempio pratico di come utilizzare Python e OpenCV 
per implementare un sistema di cattura di immagini facciali. È un passo fondamentale 
per applicazioni più avanzate di riconoscimento facciale, e la sua struttura modulare 
facilita eventuali estensioni o modifiche future.
"""

# Configura il logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)  # Crea un logger per il modulo corrente

def create_directory(directory: str) -> None:
    """
    Crea una directory se non esiste già.
    
    Parametri:
        directory (str): Il percorso della directory da creare.
    """
    try:
        # Controlla se la directory esiste già
        if not os.path.exists(directory):
            os.makedirs(directory)  # Crea la directory
            logger.info(f"Created directory: {directory}")  # Logga la creazione della directory
    except OSError as e:
        logger.error(f"Error creating directory {directory}: {e}")  # Logga eventuali errori
        raise  # Rilancia l'eccezione

def get_face_id(directory: str) -> int:
    """
    Ottiene il primo ID facciale disponibile controllando i file esistenti.
    
    Parametri:
        directory (str): Il percorso della directory delle immagini.
    Restituisce:
        int: Il prossimo ID facciale disponibile
    """
    try:
        # Se la directory non esiste, restituisce 1
        if not os.path.exists(directory):
            return 1
            
        user_ids = []  # Lista per memorizzare gli ID utente
        # Itera attraverso i file nella directory
        for filename in os.listdir(directory):
            if filename.startswith('Users-'):  # Controlla se il nome del file inizia con 'Users-'
                try:
                    number = int(filename.split('-')[1])  # Estrae l'ID dall nome del file
                    user_ids.append(number)  # Aggiunge l'ID alla lista
                except (IndexError, ValueError):
                    continue  # Ignora file non validi
                    
        return max(user_ids + [0]) + 1  # Restituisce il massimo ID + 1
    except Exception as e:
        logger.error(f"Error getting face ID: {e}")  # Logga eventuali errori
        raise  # Rilancia l'eccezione

def save_name(face_id: int, face_name: str, filename: str) -> None:
    """
    Salva il mapping nome-ID in un file JSON.
    
    Parametri:
        face_id (int): L'identificatore dell'utente
        face_name (str): Il nome dell'utente
        filename (str): Percorso del file JSON
    """
    try:
        names_json: Dict[str, str] = {}  # Dizionario per memorizzare i nomi
        if os.path.exists(filename):  # Controlla se il file esiste
            try:
                with open(filename, 'r') as fs:  # Apre il file in lettura
                    content = fs.read().strip()  # Legge il contenuto
                    if content:  # Solo se il file non è vuoto
                        names_json = json.loads(content)  # Carica il contenuto JSON
            except json.JSONDecodeError:
                logger.warning(f"Invalid JSON in {filename}, starting fresh")  # Logga un avviso se il JSON è invalido
                names_json = {}  # Inizializza un nuovo dizionario
        
        names_json[str(face_id)] = face_name  # Aggiunge il mapping ID-nome
        
        with open(filename, 'w') as fs:  # Apre il file in scrittura
            json.dump(names_json, fs, indent=4, ensure_ascii=False)  # Salva il dizionario come JSON
        logger.info(f"Saved name mapping for ID {face_id}")  # Logga il salvataggio
    except Exception as e:
        logger.error(f"Error saving name mapping: {e}")  # Logga eventuali errori
        raise  # Rilancia l'eccezione

def initialize_camera(camera_index: int = 0) -> Optional[cv2.VideoCapture]:
    """
    Inizializza la camera con gestione degli errori.
    
    Parametri:
        camera_index (int): Indice del dispositivo della camera
    Restituisce:
        cv2.VideoCapture o None: Oggetto camera inizializzato
    """
    try:
        cam = cv2.VideoCapture(camera_index)  # Inizializza la camera
        if not cam.isOpened():  # Controlla se la camera è aperta
            logger.error("Could not open webcam")  # Logga un errore se non riesce ad aprire la camera
            return None
            
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA['width'])  # Imposta la larghezza del frame
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA['height'])  # Imposta l'altezza del frame
        return cam  # Restituisce l'oggetto camera
    except Exception as e:
        logger.error(f"Error initializing camera: {e}")  # Logga eventuali errori
        return None  # Restituisce None in caso di errore

if __name__ == '__main__':
    try:
        # Inizializzazione
        create_directory(PATHS['image_dir'])  # Crea la directory per le immagini
        face_cascade = cv2.CascadeClassifier(PATHS['cascade_file'])  # Carica il classificatore facciale
        if face_cascade.empty():  # Controlla se il caricamento è andato a buon fine
            raise ValueError("Error loading cascade classifier")  # Solleva un'eccezione se non è riuscito
            
        cam = initialize_camera(CAMERA['index'])  # Inizializza la camera
        if cam is None:  # Controlla se l'inizializzazione è andata a buon fine
            raise ValueError("Failed to initialize camera")  # Solleva un'eccezione se non è riuscito
            
        # Ottiene le informazioni dell'utente
        face_name = input('\nEnter user name and press <return> -->  ').strip()  # Richiede il nome dell'utente
        if not face_name:  # Controlla se il nome è vuoto
            raise ValueError("Name cannot be empty")  # Solleva un'eccezione se il nome è vuoto
            
        face_id = get_face_id(PATHS['image_dir'])  # Ottiene un ID facciale disponibile
        save_name(face_id, face_name, PATHS['names_file'])  # Salva il mapping nome-ID
        
        logger.info(f"Initializing face capture for {face_name} (ID: {face_id})")  # Logga l'inizio della cattura
        logger.info("Look at the camera and wait...")  # Istruisce l'utente a guardare la camera
        
        count = 0  # Contatore per le immagini catturate
        while True:
            ret, img = cam.read()  # Legge un frame dalla camera
            if not ret:  # Controlla se il frame è stato catturato correttamente
                logger.warning("Failed to grab frame")  # Logga un avviso se non riesce a catturare il frame
                continue  # Continua al prossimo ciclo
                
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # Converte l'immagine a scala di grigi
            faces = face_cascade.detectMultiScale(  # Rileva i volti nell'immagine
                gray,
                scaleFactor=FACE_DETECTION['scale_factor'],  # Fattore di scala per il rilevamento
                minNeighbors=FACE_DETECTION['min_neighbors'],  # Numero minimo di vicini
                minSize=FACE_DETECTION['min_size']  # Dimensione minima del volto
            )
            
            for (x, y, w, h) in faces:  # Itera attraverso i volti rilevati
                if count < TRAINING['samples_needed']:  # Controlla se sono stati catturati abbastanza campioni
                    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Disegna un rettangolo attorno al volto
                    
                    face_img = gray[y:y+h, x:x+w]  # Estrae l'immagine del volto
                    img_path = f'./{PATHS["image_dir"]}/Users-{face_id}-{count+1}.jpg'  # Percorso per salvare l'immagine
                    cv2.imwrite(img_path, face_img)  # Salva l'immagine del volto
                    
                    count += 1  # Incrementa il contatore
                    
                    progress = f"Capturing: {count}/{TRAINING['samples_needed']}"  # Messaggio di progresso
                    cv2.putText(img, progress, (10, 30),  # Aggiunge il testo di progresso all'immagine
                               cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                else:
                    break  # Esce dal ciclo se sono stati catturati abbastanza campioni
            
            cv2.imshow('Face Capture', img)  # Mostra l'immagine con i volti catturati
            
            if cv2.waitKey(100) & 0xff == 27:  # Controlla se è stata premuta la tecla ESC
                break  # Esce dal ciclo
            if count >= TRAINING['samples_needed']:  # Controlla se sono stati catturati abbastanza campioni
                break  # Esce dal ciclo
                
        logger.info(f"Successfully captured {count} images")  # Logga il numero di immagini catturate
        
    except Exception as e:
        logger.error(f"An error occurred: {e}")  # Logga eventuali errori
        
    finally:
        if 'cam' in locals():  # Controlla se l'oggetto cam esiste
            cam.release()  # Rilascia la camera
        cv2.destroyAllWindows()  # Chiude tutte le finestre aperte
