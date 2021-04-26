import cv2

img = cv2.imread(
    "C:\\Users\\Chanuka Dinuwan\\Desktop\\Open CV\\fabian-grohs-mCj7UinqOYQ-unsplash.jpg", 1)

print(type(img))  # Coloured image
print(img.shape)

img1 = cv2.imread(
    "C:\\Users\\Chanuka Dinuwan\\Desktop\\Open CV\\fabian-grohs-mCj7UinqOYQ-unsplash.jpg", 0)

print(img1)  # Gray scale image

cv2.imshow("Coding", reasized)
cv2.waitKey(0)

cv2.destroyAllWindows()

reasized = cv2.resize(img, (600, 600))
