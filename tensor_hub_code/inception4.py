from tensorflow import keras

class InceptionV4:
    """
    InceptionV4 is a convolution neural network architecture that is one of the SOTA
    image classification architectures.
    """
    def model(self):
        """Creates InceptionV4 CNN architecture.
        Returns:
            keras-model -- Build InceptionV4 model with inceptionv4 layer A,B,C and inception reduction layer A & B.
        """
        input_t = keras.layers.Input(shape=(299, 299, 3))
        x = keras.layers.Conv2D(filters=32, kernel_size=(3, 3), padding="valid", activation="relu", strides=2)(input_t)
        x = keras.layers.Conv2D(filters=32, kernel_size=(3, 3), padding="valid", activation="relu", strides=1)(x)
        x = keras.layers.Conv2D(filters=64, kernel_size=(3, 3), padding="same", activation="relu", strides=1)(x)

        x1 = keras.layers.MaxPooling2D(pool_size=(3, 3), strides=2, padding="valid")(x)
        x2 = keras.layers.Conv2D(filters=96, kernel_size=(3, 3), padding="valid", activation="relu", strides=2)(x)
        x = keras.layers.concatenate(tensors=[x1, x2], axis=-1)

        x1 = keras.layers.Conv2D(filters=64, kernel_size=(1, 1), padding="same", activation="relu", strides=1)(x)
        x1 = keras.layers.Conv2D(filters=96, kernel_size=(3, 3), padding="valid", activation="relu", strides=1)(x1)
        x2 = keras.layers.Conv2D(filters=64, kernel_size=(1, 1), padding="same", activation="relu", strides=1)(x)
        x2 = keras.layers.Conv2D(filters=64, kernel_size=(1, 7), padding="same", activation="relu", strides=1)(x2)
        x2 = keras.layers.Conv2D(filters=64, kernel_size=(7, 1), padding="same", activation="relu", strides=1)(x2)
        x2 = keras.layers.Conv2D(filters=96, kernel_size=(3, 3), padding="valid", activation="relu", strides=1)(x2)
        x = keras.layers.concatenate([x1, x2], axis=-1)

        x1 = keras.layers.Conv2D(filters=192, kernel_size=(3, 3), padding="valid", activation="relu", strides=2)(x)
        x2 = keras.layers.MaxPooling2D(pool_size=(2, 2), strides=2, padding="valid")(x)
        x = keras.layers.concatenate(tensors=[x1, x2], axis=-1)

        for i in range(4): x = LayerA()(x)
        x = ReductionLayerA()(x)
        for i in range(7): x = LayerB()(x)
        x = ReductionLayerB()(x)
        for i in range(3): x = LayerC()(x)

        x = keras.layers.AveragePooling2D(pool_size=(8, 8))(x)
        x = keras.layers.Flatten()(x)
        x = keras.layers.Dropout(rate=0.2)(x)
        x = keras.layers.Dense(units=1000, activation="softmax")(x)

        model = keras.layers.Model(input_t, x)
        return model
