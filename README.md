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

### 輪郭描画
>>> import cv2
>>> img_color = cv2.imread('coins.jpg', cv2.IMREAD_COLOR)
>>> thresh = cv2.threshold(img_color, 127,255, cv2.THRESH_BINARY_INV)
>>> contours = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.error: OpenCV(4.5.2) :-1: error: (-5:Bad argument) in function 'findContours'
> Overload resolution failed:
>  - image is not a numerical tuple
>  - Expected Ptr<cv::UMat> for argument 'image'

```
