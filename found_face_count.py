import face_recognition

# Load the jpg file into a numpy array
image  = face_recognition.load_image_file("2.jpg")

# Find all the faces in the image
face_locations = face_recognition.face_locations(image)

# Print the number of faces detected in the image
print("I found {} face(s) in this photograph.".format(len(face_locations)))