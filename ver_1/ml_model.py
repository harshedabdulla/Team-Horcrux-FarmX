from PIL import Image, ImageOps
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
import numpy as np

image_size = [224, 224]
class_indices={}

def build_model():
    base_model = tf.keras.applications.MobileNetV2(
        input_shape=(image_size[0], image_size[1], 3),
        include_top=False,
        weights="imagenet",
    )
    base_model.trainable = False
    model = tf.keras.models.Sequential(
        [
            base_model,
            tf.keras.layers.GlobalAveragePooling2D(),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(64, activation="relu"),
            tf.keras.layers.Dense(2, activation="softmax"),
        ]
    )
    return model

def train(model, dataset_path):
    training_ds, validation_ds = get_dataset_split(
        dataset_path, validation_split=0.3, img_size=image_size
    )
    model.compile(
        optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
    )
    print(training_ds.class_indices)
    model.fit(training_ds, epochs=10, validation_data=validation_ds)

def test(model, image_path):
    data = prepare_image(image_path, target_size=image_size)
    prediction = model.predict(data).argmax()
    # pred_label = list(class_indices.keys())[prediction]
    return prediction



def prepare_image(image_path, target_size):
    data = np.ndarray(shape=(1, target_size[0], target_size[1], 3), dtype=np.float32)
    image = Image.open(image_path)
    image = ImageOps.fit(image, target_size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    normalized_image_array = image_array.astype(np.float32) / 255.0
    data[0] = normalized_image_array
    image.close()
    return data


def get_dataset_split(dataset_path, validation_split, img_size):
    img_generator = ImageDataGenerator(
        rescale=1 / 255.0,
        validation_split=validation_split,
        horizontal_flip=True,
        rotation_range=20,
        width_shift_range=0.2,
        height_shift_range=0.2,
    )

    training_ds = img_generator.flow_from_directory(
        dataset_path, target_size=img_size, subset="training"
    )
    validation_ds = img_generator.flow_from_directory(
        dataset_path, target_size=img_size, subset="validation"
    )

    return training_ds, validation_ds
