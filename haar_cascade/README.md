## Extract emotions with image and video

The software recognizes corresponding emotions in a person's face through videos, webcams, or images.  
 Based on OpenCV and haarcascade and deep learning.

![Demo](fear.PNG)

## Installation

> Install required library modules using anaconda and pip

```
conda install tensorflow==2.1.0

conda install -c conda-forge opencv

keras is installed by anaconda Navigator.

pip install pandas

pip install matplotlib

pip install scipy==1.2.0

pip install h5py==2.10.0
```

## Train models

> fer2013.tar.gz file

- [다운로드](https://www.kaggle.com/c/challenges-in-representation-learning-facial-expression-recognition-challenge/data)

- Facial Emotion Recongintion in FER2013 Dataset Using Conv

- Download and extract this file to use

## implement

```python

python extract_emotions_by_image.py

```

1. The coordinate value of the person's bounding box and the image detected by the person are received through yolo.

2. Check the coordinate values and images to see if this person is smiling and having fun.

3. If the result is happy, return true.
