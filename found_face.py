import face_recognition
import cv2

img = cv2.imread("3.jpg")
img_rgb = img[:, :, ::-1]

face_location = face_recognition.face_locations(img_rgb)  # 检测框位置
face_landmarks_list = face_recognition.face_landmarks(img_rgb)  #面部轮廓位置

for i in range(len(face_location)):#绘制检测狂
    rect = face_location[i]
    cv2.rectangle(img, (rect[3], rect[0]), (rect[1], rect[2]), (0, 0, 255), 2)

for word, face_landmarks in enumerate(face_landmarks_list):#绘制面部轮廓点
    for key, marks in face_landmarks.items():
        for i in range(len(marks)):
            point = marks[i]
            cv2.circle(img,(point[0], point[1]),2,(0,255,0))

cv2.imshow('img', img)
cv2.waitKey(0)
print("finish")