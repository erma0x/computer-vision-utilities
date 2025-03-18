from PIL import Image
import sqlite3
import cv2
from io import BytesIO  # Per scrivere l'immagine in memoria come byte stream

# Database setup
DB_NAME_VIDEO = "database_video.db"
TABLE_NAME_VIDEO = "database_video"

conn = sqlite3.connect(DB_NAME_VIDEO)
c = conn.cursor()

video_path = "uploads/video.webm"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print(f"Error: Could not open video file '{video_path}'.")

else:

    frame_count = 0
    fps = cap.get(cv2.CAP_PROP_FPS)  # Get frames per second

    while True:

        ret, frame = cap.read()  # Read each frame

        if not ret:
            break  # End of video
               
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
               
        image = Image.fromarray(frame_rgb)

        # Converti l'immagine in un buffer di memoria (byte stream)
        img_byte_array = BytesIO()
        image.save(img_byte_array, format="PNG")  # Puoi anche usare JPEG se preferisci
        img_byte_array = img_byte_array.getvalue()  # Ottieni i byte dell'immagine

        filename = video_path

        # Inserisci nel database, dove 'image' è un campo di tipo BLOB
        c.execute(f"INSERT INTO {TABLE_NAME_VIDEO} (filename, image) VALUES (?, ?)", 
                  (filename, img_byte_array))

        frame_count += 1

    print(f"Processed {frame_count} frames from the video.")

cap.release()

conn.commit()
conn.close()
