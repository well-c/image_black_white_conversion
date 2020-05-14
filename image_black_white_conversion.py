import cv2

image_path = "image.png"
image = cv2.imread(image_path)

#image = cv2.resize(image, (0,0), fx=5, fy=5)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

image_bw = cv2.threshold(image, 0, 255, cv2.THRESH_OTSU)[1]

cv2.imwrite('image_pure_bw.png', image_bw) 

image_inverted = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

cv2.imwrite('image_pure_inverted_bw.png', image_inverted) 
