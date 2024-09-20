import face_recognition

person_picture  = face_recognition.load_image_file("1.jpg")
unknown_picture = face_recognition.load_image_file("2.jpeg")

person_encoding = face_recognition.face_encodings(person_picture)[0]
unknown_encoding = face_recognition.face_encodings(unknown_picture)[0]

# 打印 person_encoding
print(person_encoding)

results = face_recognition.compare_faces([person_encoding], unknown_encoding,0.6)

if results[0] == True:
    print("found same person")
else:
    print("can not fount same person")
