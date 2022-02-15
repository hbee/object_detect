import cv2
import numpy as np
import fonctions


fond = cv2.imread("C:\\Users\\hamza\\Desktop\\jeu_photos\\bg.jpg", -1)
fond = cv2.resize(fond, (960, 722))
img = cv2.imread("C:\\Users\\hamza\\Desktop\\jeu_photos\\2m5.jpg", -1)
img = cv2.resize(img, (960, 722))

color_circle=(0, 0, 255)

seuil=20
mask=fonctions.calcul_mask(img, fond, seuil)



objets= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
for o in objets:
    ((x, y), rayon) = cv2.minEnclosingCircle(o)
    if rayon > 10.3:
        cv2.circle(img, (int(x), int(y)), 2, color_circle, 10)

cv2.imshow('fond', fond)
cv2.imshow('img', img)
cv2.imshow('mask', mask)


while True:
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
