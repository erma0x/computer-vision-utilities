# loading in modules
import sqlite3
from PIL import Image
import io

"""
Il programma estrae tutte le immagini associate a un determinato USER_ID da un database SQLite,
le converte in oggetti Image usando PIL e le memorizza in una lista.
Alla fine, chiude la connessione al database e stampa il numero di immagini recuperate.
"""

# creating file path
USER_ID = "44"
dbfile = f'./database_video.db'
TABLE_NAME = "database_video"

# Create a SQL connection to our SQLite database
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()

# reading all table names
table_list = [a for a in cur.execute(f"SELECT image FROM {TABLE_NAME} WHERE filename LIKE '%Users-{USER_ID}%'")]

image_list = []

for k,v in enumerate(table_list):
    # Fetch the BLOB data
    blob_data = table_list[k][0]

    # Convert the BLOB data to a PIL Image
    image = Image.open(io.BytesIO(blob_data))
    
    image_list.append(image)

# Be sure to close the connection
con.close()

print(len(image_list))