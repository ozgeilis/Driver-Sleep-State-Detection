import cv2
import time
import pygame
import numpy as np
pygame.mixer.init()
pygame.mixer.music.load('alarm.mp3')
count = 0

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
eyes_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

first_read = True

cap = cv2.VideoCapture(0)

ret, image = cap.read()

while ret:
    
    ret, image = cap.read()
    
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #istenilen renklere odaklanmak için gri tonlama yapar
    
    gray_scale = cv2.bilateralFilter(gray_scale, 5, 1, 1) #gürültüyü azaltır iki taraflı filtre 
  
    faces = face_cascade.detectMultiScale(gray_scale, 1.5, 5, minSize=(200, 200)) #yüz ve göz tespiti için
    if len(faces) > 0:
        for (x, y, w, h) in faces:
            image = cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)  #yüzü çerçeve içerisina alır
            
            eye_face = gray_scale[y:y + h, x:x + w]
           
            eye_face_clr = image[y:y + h, x:x + w]
            
            eyes = eyes_cascade.detectMultiScale(eye_face, 1.5, 5, minSize=(5, 5)) #yüzleri ve gözleri bulmak için
            
            if len(eyes) >= 0.5:
                count = count -1   #len fonksiyonu uzunluğu veren komuttur.
                    
                    
                    
            else:
                count = count +1
            
                cv2.imshow('image',image)  #görüntülenecek görüntüyü ifade eder
                cv2.waitKey(1) 
    if (count < 5):
       if first_read:
         pygame.mixer.music.play(-1)
         cv2.putText(image, "surucu uyanik", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (0, 255, 0), 2)

    else:
      if first_read:
       
       cv2.putText(image, "SURUCU UYUYOR", (70, 70), cv2.FONT_HERSHEY_SIMPLEX,
                                1, (0, 0,255), 2)

      else:
        cv2
    cv2.imshow('image', image)
    a = cv2.waitKey(1)           #ord fonksiyonu fonk. unicode karakter
   
    if a == ord('c'):         #c karakterine basılınca döngü kırılacak
        break
    elif a == ord('o'):
        first_read = False

cap.release()

cv2.destroyAllWindows()

