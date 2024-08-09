#My Method
import cv2

def resize_image(file_name):
    img = cv2.imread(file_name, 1)
    resize_img = cv2.resize(img, (int(100),int(100)))
    cv2.imwrite(file_name[:-4] + "_resized.jpg", resize_img)
 
resize_image("kangaroos-rain-australia.jpg")
resize_image("Lighthouse.jpg")
resize_image("Moon sinking, sun rising.jpg")

#Answer
import cv2
import glob

images = glob.glob("*.jpg")
print(images)

for image in images:
    img = cv2.imread(image, 0)
    re = cv2.resize(img, (100,100))
    cv2.imwrite("resize_" + image, re)