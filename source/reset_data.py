import os  # Importa il modulo os per interagire con il sistema operativo
import json  # Importa il modulo json per lavorare con file JSON

descrizone ="""
Il programma in questione è composto da due funzioni principali: delete_images() e delete_names(). 
La funzione delete_images() si occupa di eliminare tutti i file presenti nella cartella "images",
controllando prima se la cartella esiste. Se esiste, itera attraverso i file e li rimuove,
gestendo eventuali errori durante il processo. La funzione delete_names() 
invece svuota il contenuto di un file JSON chiamato names.json, scrivendo un oggetto vuoto al suo interno.
Entrambe le funzioni vengono chiamate nel blocco principale del programma,
che inizia con un messaggio di reset dell'ambiente. Al termine dell'esecuzione,
il programma conferma che l'ambiente di sviluppo è stato resettato con successo.
Questo script è utile per mantenere l'ordine e la pulizia in un progetto di sviluppo, 
facilitando la gestione dei file temporanei e delle informazioni non più necessarie.
"""

def delete_images(image_folder = 'images'):
    # Define the path for the "images" folder
    images_folder = os.path.join(os.getcwd(),image_folder )  # Creates the full path for the "images" folder in the current directory

    # Check if the folder exists
    if os.path.exists(images_folder):  # Verifies if the "images" folder exists
        # Delete all files in the folder
        for file_name in os.listdir(images_folder):  # Iterate over all files and folders in the "images" folder
            file_path = os.path.join(images_folder, file_name)  # Create the full path for each file or folder
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):  # Check if it's a file or symbolic link
                    os.unlink(file_path)  # Delete the file or symbolic link
                elif os.path.isdir(file_path):  # If it's a folder
                    os.rmdir(file_path)  # Delete the empty folder
            except Exception as e:  # Handle any exceptions during deletion
                print(f'Error while deleting {file_path}: {e}')  # Print error message
    else:
        print("The 'images' folder does not exist.")  # Message if the folder does not exist

    print(f"\n   Images deleted from the '/images' folder")  # Confirm the deletion of images


def delete_names(file_path = 'names.json'):
    # Open the file and clear its content
    with open(file_path, 'w') as file:  # Opens the file in write mode
        json.dump({}, file)  # Writes an empty object to the file, clearing it

    print("   All objects have been deleted from the JSON file.")  # Confirm that the file has been cleared


if __name__ == "__main__":  # Checks if the file is executed as the main program
    
    print(f"\n\tENVIRONMENT RESET ")  # Message indicating the start of the environment reset

    delete_images()  # Calls the function to delete the images
    delete_names()  # Calls the function to clear the JSON file
    
    print("   Development environment reset    ")  # Confirm the environment has been reset
