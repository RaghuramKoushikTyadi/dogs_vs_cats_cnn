import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

model = tf.keras.models.load_model("cat_dog_cnn.keras")

class_names = ["cats", "dogs"]
image_size = (180, 180)

st.title("Cat vs Dog Classifier")

uploaded_file = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image)

    img = image.resize(image_size)
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, 0)

    prediction = model.predict(img_array)[0][0]

    predicted_class = class_names[1] if prediction >= 0.5 else class_names[0]
    confidence = prediction if prediction >= 0.5 else 1 - prediction

    st.subheader(predicted_class)
    st.write(f"Confidence: {confidence:.2%}")