"""
DA USARE quando ho una cartella piena di immagini

INPUT cartella /dump/
/dump/immagine1.png
/dump/immagine2.png

OUTPUT
sposta tutte le immagini dentro
/input/lcc-fasd/LCC_FASD/LCC_FASD_{target_directory}

dove target_directory è scelta casualmente fra ["training", "evaluation", "development"]
"""

import os  # Importa il modulo os per interagire con il sistema operativo
import shutil  # Importa il modulo shutil per operazioni di alto livello su file e directory
import random  # Importa il modulo random per generare numeri casuali

path_images_input = "/spoofing-detection/images/"  # Definisce il percorso della cartella di input contenente le immagini
category = ["spoof", "real"]  # Crea una lista di categorie per le immagini

working_directory = os.getcwd()  # Ottiene la directory di lavoro corrente
print(f"Your current working directory {working_directory}")  # Stampa la directory di lavoro corrente

list_path_images_input = os.listdir(working_directory + path_images_input)  # Elenca i file nella cartella di input
path_list_images = []  # Inizializza una lista vuota per memorizzare i percorsi delle immagini
first_time = True  # Flag per controllare se è la prima volta che si esegue il ciclo

for i in list_path_images_input:  # Itera attraverso ogni elemento nella lista dei percorsi delle immagini
    
    path_single_folder = working_directory + path_images_input + i  # Costruisce il percorso della cartella corrente

    absolute_path_start = working_directory + path_images_input + i  # Costruisce il percorso assoluto del file

    path_list_images.append(absolute_path_start)  # Aggiunge il percorso assoluto alla lista dei percorsi delle immagini

    target_directory = random.choice(["training", "evaluation", "development"])  # Sceglie casualmente una delle tre directory di destinazione

    if "spoof" in i: category_target = category[0]
    if "User" in i: category_target = category[1]

    final_path = f"spoofing-detection/input/lcc-fasd/LCC_FASD/LCC_FASD_{target_directory}/{category_target}/" + i  # Costruisce il percorso finale per il file

    if first_time:  # Controlla se è la prima volta che si esegue il ciclo
        print(f"Path Iniziale ---> {absolute_path_start}")  # Stampa il percorso iniziale del file
        print(f"Path Finale   ---> {final_path}")  # Stampa il percorso finale del file

        answer = input("Controllare il corretto spostamento del file, Vuoi uscire? (premere y) ")  # Chiede all'utente di confermare il movimento del file
        if answer.lower() == "y":  # Se l'utente risponde 'y'
            exit()  # Esce dal programma
            
        first_time = False  # Imposta il flag a False dopo la prima esecuzione
    
    shutil.move(absolute_path_start, final_path)  # Sposta il file dal percorso iniziale a quello finale
