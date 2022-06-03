import cv2
import numpy as np
import sys
from keras.models import load_model
from statistics import mode
from haar_cascade.utils.datasets import get_labels
from haar_cascade.utils.preprocessor import preprocess_input

emotion_model_path = './haar_cascade/models/emotion_model.hdf5'
emotion_labels = get_labels('fer2013')
emotion_classifier = load_model(emotion_model_path)
emotion_target_size = emotion_classifier.input_shape[1:3]

smile_cascade = cv2.CascadeClassifier('./haar_cascade/smile_cascade.xml')

def get_emotion_by_image(image, coordinates):
    bgr_image = cv2.imread(image)
    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
    for coordinate in coordinates.values():
        if coordinate == True:
            continue
        x1 = int(coordinate[0])
        y1 = int(coordinate[1])
        x2 = int(coordinate[2])
        y2 = int(coordinate[3])

        

        gray_face = gray_image[y1:y2, x1:x2]
        try:
            smile = smile_cascade.detectMultiScale(gray_face, 1.8, 24)
            #gray_face = cv2.resize(gray_face, (emotion_target_size))
        except:
            continue
        
        if len(smile) != 0:
            return True
        #gray_face = preprocess_input(gray_face, True)
        #gray_face = np.expand_dims(gray_face, 0)
        #gray_face = np.expand_dims(gray_face, -1)
        #emotion_prediction = emotion_classifier.predict(gray_face)
        #emotion_probability = np.max(emotion_prediction)
        #emotion_label_arg = np.argmax(emotion_prediction)
        #emotion_text = emotion_labels[emotion_label_arg]
      
        #if emotion_text == 'happy':
        #    return True
    return False


## test

# result = get_emotion_by_image('./haar_cascade/demo/test.jpg',{'detect': True, 0: [648.0, 526.0, 753.0, 680.0], 1: [657.0, 313.0, 793.0, 618.0], 2: [417.0, 309.0, 548.0, 562.0], 3: [282.0, 373.0, 422.0, 764.0], 4: [113.0, 383.0, 279.0, 606.0], 5: [522.0, 411.0, 645.0, 681.0], 6: [412.0, 531.0, 564.0, 845.0], 7: [154.0, 555.0, 331.0, 855.0], 8: [613.0, 602.0, 892.0, 853.0]})

# if result == True :
#     print("happy")
# else :
#     print("unhappy")
