import cv2
img = cv2.imread("input.jpg")

for i in img:
    for j in i:
        if j[2] > (j[0] + j[1])*1.2:
            j[0] = 0
            j[1] = 255
            j[2] = 0
cv2.imwrite("output.jpg",img)
ouput = cv2.imread("output.jpg")
cv2.imshow("anh sau khi luu",ouput)
cv2.waitKey(0)
cv2.destroyAllWindows()