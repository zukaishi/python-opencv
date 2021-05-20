# python-opencv

### 準備
```
pip3 install opencv-python
pip3 install numpy
```

### バージョン確認
```
python3
>>> import cv2
>>> cv2.__version__
'4.5.2'
```

### グレイにしてウィンドウ表示
python3 01_window.py

![pokemon](https://user-images.githubusercontent.com/22611735/118332001-5f86b780-b544-11eb-9b53-8e5a321426aa.png)

<img width="762" alt="スクリーンショット 2021-05-19 6 07 33" src="https://user-images.githubusercontent.com/22611735/118723597-94f31400-b868-11eb-9858-e1fe63aff1de.png">


### 輪郭描画
python3 02_contours.py

![pokemon](https://user-images.githubusercontent.com/22611735/118332001-5f86b780-b544-11eb-9b53-8e5a321426aa.png)

![pokemon_save](https://user-images.githubusercontent.com/22611735/118332007-631a3e80-b544-11eb-92fe-d9421873cc34.png)

### 顔検出
python3 03_cascade.py

![girl](https://user-images.githubusercontent.com/22611735/118559122-762a4a00-b7a2-11eb-960b-eb7809447406.png)

![gril_cascade_save](https://user-images.githubusercontent.com/22611735/118559131-79bdd100-b7a2-11eb-93aa-03d2ceb8db55.png)

### OpenFace(顔照合)
```
docker pull bamos/openface

docker run -p 9000:9000 -p 8000:8000 -t -i bamos/openface /bin/bash

cd /root/openface
```
```
./demos/compare.py images/examples/{lennon*,clapton*}

Comparing images/examples/lennon-1.jpg with images/examples/lennon-2.jpg.
  + Squared l2 distance between representations: 0.763
Comparing images/examples/lennon-1.jpg with images/examples/clapton-1.jpg.
  + Squared l2 distance between representations: 1.132
Comparing images/examples/lennon-1.jpg with images/examples/clapton-2.jpg.
  + Squared l2 distance between representations: 1.145
Comparing images/examples/lennon-2.jpg with images/examples/clapton-1.jpg.
  + Squared l2 distance between representations: 1.447
Comparing images/examples/lennon-2.jpg with images/examples/clapton-2.jpg.
  + Squared l2 distance between representations: 1.521
Comparing images/examples/clapton-1.jpg with images/examples/clapton-2.jpg.
  + Squared l2 distance between representations: 0.318
```

```
./demos/classifier.py infer models/openface/celeb-classifier.nn4.small2.v1.pkl ./images/examples/carell.jpg

=== ./images/examples/carell.jpg ===
/root/.local/lib/python2.7/site-packages/sklearn/preprocessing/label.py:166: DeprecationWarning: The truth value of an empty array is ambiguous. Returning False, but in future this will result in an error. Use `array.size > 0` to check that an array is not empty.
  if diff:
Predict SteveCarell with 0.97 confidence.
```
