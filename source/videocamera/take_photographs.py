import cv2
import os

"""
Il programma scatta immagini dalla videocamera e le salva in una cartella,
 assegnando loro un nome univoco basato su un numero di utente. 
 Se un nome esiste già, il numero dell'utente viene incrementato. 
 Le immagini vengono salvate in una cartella specificata 
 e il processo termina dopo un numero definito di scatti.
"""

def get_unique_img_name(user_number, i, output_dir):
    # Function to get a unique name for the image
    img_name = os.path.join(output_dir, f'Users-{user_number}-{i+1}.jpg')
    while os.path.exists(img_name):  # Check if the file already exists
        user_number += 1  # Increment the user number to get a different name
        img_name = os.path.join(output_dir, f'Users-{user_number}-{i+1}.jpg')
    return img_name, user_number


def take_photographs(output_dir = 'images', camera = 0, number_of_images = 100):
    # Initialize the user number
    user_number = 1

    # Create the directory to save images if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Initialize the camera
    cap = cv2.VideoCapture(camera)  # default = 0

    # Check if the camera is opened
    if not cap.isOpened():
        print("Error: Unable to open the camera.")
        exit()

    # Capture images
    for i in range(number_of_images):
        
        ret, frame = cap.read()  # Read a frame from the camera

        if not ret:
            print("Error: Unable to read the frame.")
            break

        # Get a unique name for the image
        img_name, user_number = get_unique_img_name(user_number, i, output_dir)
        
        # Save the image
        cv2.imwrite(img_name, frame)

        print(f' {int( i+1 / number_of_images * 100 )} %   {img_name}')

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    
    take_photographs(output_dir = 'images', camera = 0, number_of_images = 100)
