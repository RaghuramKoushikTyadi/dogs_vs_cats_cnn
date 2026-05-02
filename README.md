Dogs vs Cats CNN Classifier

This project is a deep learning application that classifies images as
either a dog or a cat using a Convolutional Neural Network (CNN). It
also includes a Streamlit-based web interface for real-time predictions.

------------------------------------------------------------------------

Overview

-   Model: Convolutional Neural Network (TensorFlow/Keras)
-   Task: Binary image classification (Dog vs Cat)
-   Interface: Streamlit web app
-   Input: Image upload
-   Output: Predicted class with confidence score

------------------------------------------------------------------------

Project Structure

.
front.py -> Streamlit UI for prediction
model.py -> Model training and saving
clean_data.py -> Data preprocessing
split_data.py -> Dataset splitting

------------------------------------------------------------------------

How It Works

1.  User uploads an image through the Streamlit interface
2.  Image is resized and converted into an array
3.  Model predicts probability
4.  Prediction is mapped to Dog or Cat
5.  Confidence score is displayed

------------------------------------------------------------------------

Installation

(Optional) Create a virtual environment:

python -m venv tfenv
tfenv

Install dependencies:

pip install -r requirements.txt

------------------------------------------------------------------------

Running the Application

streamlit run front.py

After running, open the local URL shown in the terminal.

------------------------------------------------------------------------

Model Details

-   Input size: (replace with your size, e.g., 150x150)
-   Output layer: Single neuron with sigmoid activation
-   Loss function: Binary crossentropy
-   Optimizer: Adam

------------------------------------------------------------------------

Notes

-   Dataset and virtual environment are not included in this repository
-   Model file may be excluded if it is too large

------------------------------------------------------------------------

Future Improvements

-   Use transfer learning (MobileNet, ResNet, etc.)
-   Improve accuracy with data augmentation
-   Deploy the application online
