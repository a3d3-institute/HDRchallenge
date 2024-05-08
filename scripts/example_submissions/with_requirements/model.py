import numpy as np

class Model:
    def __init__(self):
        # You could include a constructor to initialize your model here, but all calls will be made to the load method
        self.clf = None 

    def predict(self, X):
        # This method should accept an input of any size (of the given input format) and return predictions appropriately
        return np.array([0 for _ in range(len(X))])

    def load(self):
        # This method should load your pretrained model from wherever you have it saved
        pass

