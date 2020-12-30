import cv2

img=cv2.imread('Samples/image1.jpg', 1)


print(img)

for i in range (0,3):
    for j in range (0,3):
        for k in range(0,3):

            if (img[i][j][0]==253 and img[i][j][1]==0 and img[i][j][2]==0 ):
                print("this image has blue")


"""
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#dont try to maximize the image!!!!!! 
"""