import PIL
PIL.__version__
import tf_keras as keras  # Importowanie tf-keras – wersja Keras kompatybilna z modelami .h5
from tf_keras.models import load_model  # Importowanie funkcji load_model z tf_keras, która pomaga nam z otwarciem modelu
from PIL import Image, ImageOps  # Instalowanie pillow zamiast PIL
import numpy as np
def get_class(model_path="Path to model", labels_path="Path to labels", image_path="Path to image"):

    np.set_printoptions(suppress=True)
    model = load_model(model_path, compile=False)
    class_names = open(labels_path, "r").readlines()
    image = Image.open(image_path).convert("RGB")

    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) 

    data[0] = normalized_image_array
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]
    
    return class_name[2:], confidence_score