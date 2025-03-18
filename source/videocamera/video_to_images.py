import cv2
import sqlite3
from PIL import Image
import numpy as np
from io import BytesIO

video_path = "./uploads/video.mp4"
DB_NAME = "database_video.db"
TABLE_NAME = "database_video"
user_id = 1


# Open the video file using OpenCV
cap = cv2.VideoCapture(video_path)

# Check if video was successfully opened
if not cap.isOpened():
    print("Error: Unable to open video file")

else:
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    
    counter = 0
    
    while True:
        
        counter += 1
        id += 1
    
        ret, frame = cap.read()

        if not ret:
            break
                
        pil_image = Image.fromarray( cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) )
        
        # Convert PIL image to byte stream
        byte_io = BytesIO()
        pil_image.save(byte_io, format='JPEG')

        # Go to the beginning of the byte stream
        byte_io.seek(0) 
        
        filename = f"Users-{user_id}-{counter}.jpg"
        
        # Insert the frame as a BLOB into the database
        c.execute(f"INSERT INTO {TABLE_NAME} (filename, image) VALUES (?, ?)", 
                  (filename, byte_io.read()))
        
        conn.commit()

    cap.release()
    conn.close()
    print("Frames extracted and saved to database.")
