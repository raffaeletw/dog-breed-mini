import numpy as np
import streamlit as st
import cv2
from keras.models import load_model

#Loading the model
model = load_model("dog_breed.h5")

#Name of the classes
CLASS_NAMES = ["Scottish Deerhoung", "Maltese Dog", "Bernese Mountain dog"]

st.title("Dog Breed Prediction")
st.markdown("Upload an image of the dog")

dog_image = st.file_uploader("Chooìse an image:", type="png")
submit = st.button("Predict")

if submit:
    if dog_image is not None:

        #converting to an opencv image
        file_bytes = np.asarray(bytearray(dog_image.read()), dtype = np.uint8)
        opencv_image = cv2.imdecode(file_bytes, 1)

        #let's display the image
        st.image(opencv_image, channels="BGR")
        opencv_image = cv2.resize(opencv_image, (224, 224))
        opencv_image.shape = (1,224, 224, 3)

        #Let's make a prediction
        Y_pred = model.predict(opencv_image)

        st.title(str("The dog breed is "+CLASS_NAMES[np.argmax(Y_pred)]))

        

