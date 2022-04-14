import cv2
import face_recognition
import os


img = cv2.imread("Messi1.webp")
rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_encoding = face_recognition.face_encodings(rgb_img)[0]

directory = 'images/'
flag = True

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        img2 = cv2.imread(f)
        rgb_img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
        img_encoding2 = face_recognition.face_encodings(rgb_img2)[0]

        result = face_recognition.compare_faces([img_encoding], img_encoding2)

        if result[0]:
            basename = os.path.basename(f)
            (filename, ext) = os.path.splitext(basename)
            print(filename)
            flag = False

if flag:
    print("Not Found")





