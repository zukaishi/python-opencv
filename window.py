import cv2
img_color = cv2.imread('./image/pokemon.png')
img_gray = cv2.imread('./image/pokemon.png', cv2.IMREAD_GRAYSCALE)

cv2.imshow('gray', img_gray)
cv2.waitKey(0)

cv2.destroyWindow('gray') 
cv2.waitKey(1)

import cv2
img_color = cv2.imread('coins.jpg', cv2.IMREAD_COLOR)
cv2.imwrite('./image/pokemon_save.png', img_color)