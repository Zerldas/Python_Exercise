import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow.keras import models, layers
import tensorflow_datasets as tfds
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import train_test_split

class LetterModel:
    def __init__(self):
        self.model = None
        self.history = None
        self.input_shape = (28, 28, 1)
        self.num_classes = 26

    def _convert_to_numpy(self, dataset):
        # Chuyển tf dataset thành numpy array
        X, y = [], []

        for image, label in tfds.as_numpy(dataset):
            X.append(image)
            y.append(label)
        return np.array(X), np.array(y)

    def load_data(self):
        (ds_train, ds_test), ds_info = tfds.load(
            'emnist/letters',
            split=['train', 'test'],
            shuffle_files=True, # Không đọc theo thứ tự
            as_supervised=True, # Dùng để nhận dữ liệu dạng (image, label)
            with_info=True,
            data_dir=r"D:\New_Project\Python\HK1_2025-2026\CNN(week5)\data"
        )

        # Chuyển dữ liệu sang numpy array
        X_train, y_train = self._convert_to_numpy(ds_train)
        X_test, y_test = self._convert_to_numpy(ds_test)

        # Đưa dữ liệu về giá trị [0, 1]
        X_train = X_train.astype('float32') / 255.0
        X_test = X_test.astype('float32') / 255.0

        # Thêm 1 chiều cho tập dữ liệu
        X_train = np.expand_dims(X_train, -1)
        X_test = np.expand_dims(X_test, -1)

        # CNN Keras chỉ có 25 labels, nhưng dataset lại có từ 1-26
        y_train -= 1
        y_test -= 1 

        # One-hot
        y_train = to_categorical(y_train, self.num_classes)
        y_test = to_categorical(y_test, self.num_classes)

        # Lấy 10% dữ liệu làm valiđation
        X_train, X_val, y_train, y_val = train_test_split(
            X_train, y_train, test_size=0.1, 
            random_state=42
        ) 

        print("Train: ", X_train.shape)
        print("Valid: ", X_val.shape)
        print("Test: ", X_test.shape)

        return (X_train, y_train), (X_val, y_val), (X_test, y_test)
    

    def build_model(self):
        self.model = models.Sequential([
            layers.Conv2D(32, (3, 3), activation='relu', input_shape=self.input_shape),
            layers.MaxPooling2D((2, 2)),
            layers.Conv2D(64, (3, 3), activation='relu'),
            layers.MaxPooling2D((2, 2)),
            layers.Flatten(),
            layers.Dense(128, activation='relu'),
            layers.Dense(self.num_classes, activation='softmax')
        ])

        self.model.compile(
            optimizer='adam',
            loss='categorical_crossentropy',
            metrics=['accuracy']
        )

    def train(self, X_train, y_train, X_val, y_val, epochs=10, batch_size=128):
        self.history = self.model.fit(
            X_train, y_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=(X_val, y_val),
            verbose=1
        )

    def evaluate(self, X_test, y_test):
        test_loss, test_acc = self.model.evaluate(X_test, y_test, verbose=0)
        print(f"Test accuracy: {test_acc:.4f}")
        print(f"Test loss: {test_loss:.4f}")


    def plot_history(self):
        plt.plot(self.history.history['accuracy'], label='Train Accuracy')
        plt.plot(self.history.history['val_accuracy'], label='Validation Accuracy')
        plt.title('Training History (EMNIST Letters)')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.show()