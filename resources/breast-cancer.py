from flask_restful import Resource
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

class Prediction(Resource):

    def get(self, sample):
        with open('./models/breast_cancer_model.sav', 'rb') as f:
            loaded_model = pickle.load(f)

        prediction = loaded_model.predict(sample)
        confidence = loaded_model.predict_proba(sample)[0][1])

        return {'malignant_status': prediction, 'confidence': confidence}
