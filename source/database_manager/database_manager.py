import os
import sqlite3
from PIL import Image
import io

"""
Il programma carica immagini .jpg da una cartella, 
le converte in formato binario e le salva in un database SQLite.
Crea una tabella con il nome del file e i dati binari dell'immagine.
Dopo aver inserito tutte le immagini, conferma il completamento dell'operazione.
"""

# Percorso della cartella che contiene le immagini .jpg
folder_path_images = 'immagini_documenti'

# Nome della tabella che contiene le immagini .jpg
NOME_TABELLA = "database_documents"

# Estensioni delle immagini
ESTENSIONE_IMMAGINI = ".jpg"

# Creare una connessione al database SQLite (se non esiste, verrà creato)
conn = sqlite3.connect(f'{NOME_TABELLA}.db')
cur = conn.cursor()

# Creare una tabella per le immagini
cur.execute(f'''
CREATE TABLE IF NOT EXISTS {NOME_TABELLA} (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    image BLOB)
''')

# Funzione per convertire un'immagine in formato binario
def image_to_binary(image_path):
    with open(image_path, 'rb') as file:
        img_binary = file.read()
    return img_binary

# Iterare sulle immagini nella cartella e inserirle nel database
for filename in os.listdir(folder_path_images):
    if filename.endswith(ESTENSIONE_IMMAGINI):
        file_path = os.path.join(folder_path_images, filename)
        img_binary = image_to_binary(file_path)
        
        # 6. Inserire nel database
        cur.execute(f"INSERT INTO {NOME_TABELLA} (filename, image) VALUES (?, ?)", (filename, img_binary))

# Salvare (commit) e chiudere la connessione al database
conn.commit()
conn.close()

print(f"Le immagini {ESTENSIONE_IMMAGINI} sono state inserite correttamete nel database SQL.")