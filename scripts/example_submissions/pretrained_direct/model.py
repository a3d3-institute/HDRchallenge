import tensorflow as tf
import os

class Model:
    def __init__(self):
        # You could include a constructor to initialize your model here, but all calls will be made to the load method
        self.clf = None 

    def predict(self, X):
        # This method should accept an input of any size (of the given input format) and return predictions appropriately
        return [i[0] for i in self.clf.predict(X)]

    def load(self):
        # This method should load your pretrained model from wherever you have it saved
        self.clf = tf.keras.models.load_model(os.path.join(os.path.dirname(__file__), 'trained_model.keras'))

