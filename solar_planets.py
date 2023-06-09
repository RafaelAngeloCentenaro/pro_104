import cv2
img =cv2.imread("planetinhas.jpg")
cv2.putText(img,
            "Sol",
            (100,80),
            cv2.FONT_HERSHEY_COMPLEX,
            2,
            (0,0,255)
            )
cv2.putText(img,
            "Mercurio",
            (50,190),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )
cv2.putText(img,
            "Venus",
            (175,275),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )
cv2.putText(img,
            "Terra",
            (275,170),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )
cv2.putText(img,
            "Marte",
            (350,275),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )
cv2.putText(img,
            "Jupter",
            (450,80),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )
cv2.putText(img,
            "Saturno",
            (700,300),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )
cv2.putText(img,
            "Urano",
            (900,150),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )
cv2.putText(img,
            "Netuno",
            (1100,300),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,255,255)
            )
cv2.imshow("SistemaSolar",img)
cv2.waitKey(0)