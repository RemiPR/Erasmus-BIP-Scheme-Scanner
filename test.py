
import os
import numpy as np
import cv2
import fitz  # PyMuPDF
import tensorflow as tf
from tqdm import tqdm
import matplotlib.pyplot as plt
 
output_dir = 'extracted_images'
os.makedirs(output_dir, exist_ok=True)
 
def extract_images_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    image_paths = []
   
    for i in tqdm(range(len(doc)), desc="Extracting images from PDF"):
        page = doc[i]
        pix = page.get_pixmap()
        image_path = os.path.join(output_dir, f'image_{i}.png')
        pix.save(image_path)
        image_paths.append(image_path)
   
    return image_paths
 
def preprocess_image(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY_INV)
    return binary
 
def create_model(input_shape, num_classes):
    model = tf.keras.Sequential([
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu', input_shape=input_shape),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(64, activation='relu'),
        tf.keras.layers.Dense(num_classes, activation='softmax')
    ])
    model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    return model
 
def train_model(X_train, y_train, num_classes):
    model = create_model((64, 64, 1), num_classes)
    model.fit(X_train, y_train, epochs=10, batch_size=32)
    return model
 
def recognize_schemes(model, image_paths, class_labels):
    for img_path in image_paths:
        processed_image = preprocess_image(img_path)
        resized_image = cv2.resize(processed_image, (64, 64)).reshape(-1, 64, 64, 1).astype('float32') / 255.0
       
        prediction = model.predict(resized_image)
        predicted_class = np.argmax(prediction)
        print(f"Image: {img_path} -> Recognized class: {class_labels[predicted_class]}")
 
def recognize_new_circuit(model, circuit_image_path, class_labels):
    processed_image = preprocess_image(circuit_image_path)
    resized_image = cv2.resize(processed_image, (64, 64)).reshape(-1, 64, 64, 1).astype('float32') / 255.0
   
    prediction = model.predict(resized_image)
    predicted_class = np.argmax(prediction)
 
    print(f"Circuit Image: {circuit_image_path} -> Recognized class: {class_labels[predicted_class]}")
 
    original_image = cv2.imread(circuit_image_path)
    plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
    plt.title(f"Recognized class: {class_labels[predicted_class]}")
    plt.axis('off')
    plt.show()
 
def main():
    pdf_path = 'isa5.1.pdf'
    print("Extracting images from PDF...")
    image_paths = extract_images_from_pdf(pdf_path)
 
    print("Preprocessing images...")
    processed_images = [preprocess_image(img_path) for img_path in tqdm(image_paths, desc="Processing images")]
 
    print("Preparing data for training...")
    X_train = np.array([cv2.resize(img, (64, 64)) for img in processed_images])
    X_train = X_train.reshape(-1, 64, 64, 1).astype('float32') / 255.0
 
    y_train = np.array([0] * len(X_train))  # Update with actual labels
    num_classes = 1  # Update with actual number of classes
    print("Creating and training model...")
    model = train_model(X_train, y_train, num_classes)
   
    print("Training completed!")
 
    class_labels = ['Class 0']  # Update with your actual class labels
    print("Recognizing schemes...")
    recognize_schemes(model, image_paths, class_labels)
 
    # Recognize a new circuit diagram
    new_circuit_image_path = 'IMG_2896.jpg'  # Set the path to your circuit image
    print("Recognizing new circuit diagram...")
    recognize_new_circuit(model, new_circuit_image_path, class_labels)
 
if __name__ == '__main__':
    main()
 