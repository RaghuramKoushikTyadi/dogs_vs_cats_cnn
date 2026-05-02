import tensorflow as tf
from tensorflow import keras
import numpy as np
from tensorflow.keras import layers, models
from pathlib import Path

image_size = (180, 180)
batch_size = 32
epochs = 15

def load_data(data_dir):
    data_dir = Path(data_dir)
    train_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir / "train",
        image_size=image_size,
        batch_size=batch_size,
        label_mode="binary"
    )
    val_ds = tf.keras.utils.image_dataset_from_directory(
        data_dir / "val",
        image_size=image_size,
        batch_size=batch_size,
        label_mode="binary"
    )
    return train_ds, val_ds

def build_model():
    model = models.Sequential([
        layers.Input(shape=(180, 180, 3)),
        layers.Rescaling(1./255),
        layers.Conv2D(32, 3, activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(64, 3, activation="relu"),
        layers.MaxPooling2D(),
        layers.Conv2D(128, 3, activation="relu"),
        layers.MaxPooling2D(),
        layers.Flatten(),
        layers.Dense(128, activation="relu"),
        layers.Dense(1, activation="sigmoid")
    ])
    model.compile(
        optimizer="adam",
        loss="binary_crossentropy",
        metrics=["accuracy"]
    )
    return model

train_ds,val_ds=load_data("dataset")

model=build_model()
model.fit(train_ds, validation_data=val_ds, epochs=epochs)

model.save("cat_dog_cnn.keras")