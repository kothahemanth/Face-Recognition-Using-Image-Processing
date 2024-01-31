import tkinter as tk
from tkinter import filedialog
import face_recognition as fr
import cv2
import numpy as np
import os

def browse_file():
    global test_image_path
    test_image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp")])
    test_image_entry.delete(0, tk.END)
    test_image_entry.insert(0, test_image_path)

def recognize_faces():
    path = "./train/"
    known_names = []
    known_name_encodings = []

    images = os.listdir(path)
    for _ in images:
        image = fr.load_image_file(path + _)
        image_path = path + _
        encoding = fr.face_encodings(image)[0]

        known_name_encodings.append(encoding)
        known_names.append(os.path.splitext(os.path.basename(image_path))[0].capitalize())

    test_image = test_image_path
    image = cv2.imread(test_image)

    face_locations = fr.face_locations(image)
    face_encodings = fr.face_encodings(image, face_locations)

    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        matches = fr.compare_faces(known_name_encodings, face_encoding)
        name = ""

        face_distances = fr.face_distance(known_name_encodings, face_encoding)
        best_match = np.argmin(face_distances)

        if matches[best_match]:
            name = known_names[best_match]

        cv2.rectangle(image, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.rectangle(image, (left, bottom - 15), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(image, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    cv2.imshow("Result", image)
    cv2.imwrite("./output.jpg", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Create the main window
root = tk.Tk()
root.title("Face Recognition")
root.geometry("400x300")
# Test image selection
test_image_label = tk.Label(root, text="Select Test Image:")
test_image_label.pack()
test_image_entry = tk.Entry(root)
test_image_entry.pack()
browse_button = tk.Button(root, text="Browse", command=browse_file)
browse_button.pack()

# Recognize faces button
recognize_button = tk.Button(root, text="Recognize Faces", command=recognize_faces)
recognize_button.pack()

root.mainloop()
