# python-opencv

```
準備
pip3 install opencv-python
pip3 install numpy

### バージョン確認
python3
>>> import cv2
>>> cv2.__version__
'4.5.2'

### 画像表示
python3
>>> import cv2
>>> img_color = cv2.imread('./image/pokemon.png')
>>> img_gray = cv2.imread('./image/pokemon.png', cv2.IMREAD_GRAYSCALE)

>>> cv2.imshow('gray', img_gray)
>>> cv2.waitKey(0)

>>> cv2.destroyWindow('gray') 
>>> cv2.waitKey(1)

### 画像コピー
>>> import cv2
>>> img_color = cv2.imread('coins.jpg', cv2.IMREAD_COLOR)
>>> cv2.imwrite('./image/pokemon_save.png', img_color)

```
### 輪郭描画
python3 contours.py

![pokemon](https://user-images.githubusercontent.com/22611735/118332001-5f86b780-b544-11eb-9b53-8e5a321426aa.png)

![pokemon_save](https://user-images.githubusercontent.com/22611735/118332007-631a3e80-b544-11eb-92fe-d9421873cc34.png)

### 顔検出
python3 cascade.py

![girl](https://user-images.githubusercontent.com/22611735/118559122-762a4a00-b7a2-11eb-960b-eb7809447406.png)

![gril_cascade_save](https://user-images.githubusercontent.com/22611735/118559131-79bdd100-b7a2-11eb-93aa-03d2ceb8db55.png)

