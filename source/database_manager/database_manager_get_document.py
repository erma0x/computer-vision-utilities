import sqlite3
import numpy as np
from PIL import Image
import io

"""
Il programma estrae un'immagine associata a un determinato USER_ID da un database SQLite.
Carica l'immagine come BLOB, la converte in un array NumPy e ne visualizza la forma.
Mostra l'immagine e chiude la connessione al database, stampando anche i dettagli dell'immagine recuperata.
"""


USER_ID = 3

# creating file path
dbfile = f'./database_documents.db'
TABLE_NAME = "database_documents"

# Create a SQL connection to our SQLite database
con = sqlite3.connect(dbfile)

# creating cursor
cur = con.cursor()

# reading all table names
table_list = [a for a in cur.execute(f"SELECT image FROM {TABLE_NAME} WHERE filename LIKE '%id{str(USER_ID)}.jpg%'")]

# Fetch the BLOB data
blob_data = table_list[0][0]

# Convert the BLOB data to a PIL Image
image = Image.open(io.BytesIO(blob_data))

# Convert the image to a NumPy array
np_array = np.array(image)

# Check the shape of the image
print(f"Image shape: {np_array.shape}")

# Visualize the image using PIL's built-in show method
image.show()

# Be sure to close the connection
con.close()

# Print out the results
print(table_list[0])
print("-" * 100)
print("Images captured from SQL database -> ", len(table_list))
