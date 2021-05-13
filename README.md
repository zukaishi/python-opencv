# python-opencv

```
pip3 install opencv-python
pip3 install numpy

### バージョン確認
python3
>>> import cv2
>>> cv2.__version__

### 画像表示
python3
>>> import cv2
>>> img_color = cv2.imread('coins.jpg')
>>> img_gray = cv2.imread('coins.jpg', cv2.IMREAD_GRAYSCALE)

>>> cv2.imshow('gray', img_gray)
>>> cv2.waitKey(0)

>>> cv2.destroyWindow('gray') 
>>> cv2.waitKey(1)

### 画像コピー
>>> import cv2
>>> img_color = cv2.imread('coins.jpg', cv2.IMREAD_COLOR)
>>> cv2.imwrite('save.png', img_color)
```
### 輪郭描画
contours.py
