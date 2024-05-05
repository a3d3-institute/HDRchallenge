import tensorflow as tf
import json
import os

class Model:
    def __init__(self):
        # You could include a constructor to initialize your model here, but all calls will be made to the load method
        self.clf = None 

    def predict(self, X):
        # This method should accept an input of any size (of the given input format) and return predictions appropriately
        return self.clf.predict(X)

    def load(self):
        # This method should load your pretrained model from wherever you have it saved
        print(os.path.dirname(__file__))
        print(os.listdir(os.path.dirname(__file__)))
        with open(os.path.join(os.path.dirname(__file__), 'config.json'), 'r') as file:
            for line in file:
                self.clf = tf.keras.models.model_from_json(line)
        self.clf.load_weights(os.path.join(os.path.dirname(__file__), 'model.weights.h5'))

