import cv2

img = cv2.imread("solar-system.jpg")

cv2.putText(img,"Sun",(20,60),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 3,
            color = (0,0,255)
            )

cv2.putText(img,"Mercury",(120,180),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
            )

cv2.putText(img,"Venus",(197,255),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
            )

cv2.putText(img,"Earth",(290,260),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
            )

cv2.putText(img,"Mars",(390,250),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
            )

cv2.putText(img,"Jupiter",(490,80),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
            )

cv2.putText(img,"Saturn",(690,120),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
            )

cv2.putText(img,"Neptune",(950,140),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
            )

cv2.putText(img,"Uranus",(1100,150),
            fontFace = cv2.FONT_HERSHEY_COMPLEX_SMALL,
            fontScale = 0.5,
            color = (255,255,255)
            )

cv2.imshow("Output",img)

cv2.waitKey(0)