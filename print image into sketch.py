import cv2
image = cv2.imread("C:\\Users\\rajsu\Downloads\\WhatsApp Image 2022-12-18 at 2.04.17 PM.jpeg") 
grey_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
invert = cv2.bitwise_not(grey_img) 
blur = cv2.GaussianBlur(invert, (111, 111), 0)
invertedblur = cv2.bitwise_not(blur)
sketch = cv2.divide(grey_img, invertedblur, scale=256.0)
cv2.imwrite("sketch.png", sketch) 
