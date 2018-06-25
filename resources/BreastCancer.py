from flask import request, jsonify
from flask_restful import Resource
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
import numpy as np

class BreastCancerPrediction(Resource):

    def post(self):

        print("Flag 2")
        sample_json = request.json

        sample_dict = { "radius_mean" : sample_json['radius_mean'],
                        "texture_mean" :	sample_json['texture_mean'],
                        "perimeter_mean" : sample_json['perimeter_mean'],
                        "area_mean" :	sample_json['area_mean'],
                        "smoothness_mean" : sample_json['smoothness_mean'],
                        "compactness_mean" :sample_json['compactness_mean'],
                        "concavity_mean" : sample_json['concavity_mean'],
                        "concave_points_mean" : sample_json['concave_points_mean'],
                        "symmetry_mean" : sample_json['symmetry_mean'],
                        "fractal_dimension_mean" : sample_json['fractal_dimension_mean'],
                        "radius_standard_error" : sample_json['radius_standard_error'],
                        "texture_standard_error" : sample_json['texture_standard_error'],
                        "perimeter_standard_error" : sample_json['perimeter_standard_error'],
                        "area_standard_error" : sample_json['area_standard_error'],
                        "smoothness_standard_error" : sample_json['smoothness_standard_error'],
                        "compactness_standard_error" : sample_json['compactness_standard_error'],
                        "concavity_standard_error" : sample_json['concavity_standard_error'],
                        "concave_points_standard_error" : sample_json['concave_points_standard_error'],
                        "symmetry_standard_error" : sample_json['symmetry_standard_error'],
                        "fractal_dimension_standard_error" : sample_json['fractal_dimension_standard_error'],
                        "radius_worst" : sample_json['radius_worst'],
                        "texture_worst" : sample_json['texture_worst'],
                        "perimeter_worst" : sample_json['perimeter_worst'],
                        "area_worst" : sample_json['area_worst'],
                        "smoothness_worst" : sample_json['smoothness_worst'],
                        "compactness_worst" : sample_json['compactness_worst'],
                        "concavity_worst" : sample_json['concavity_worst'],
                        "concave_points_worst" : sample_json['concave_points_worst'],
                        "symmetry_worst" : sample_json['symmetry_worst'],
                        "fractal_dimension_worst" : sample_json['fractal_dimension_worst'] }


        name = ['data']
        format = ['f']
        dtype = dict(names=name, formats=format)

        print("Flag 1")

        sample = np.array(list(sample_dict.values()), dtype=np.float)

        sample = sample.reshape(1, -1)

        print("Flag3")

        with open('./models/breast_cancer_model.sav', 'rb') as f:
            loaded_model = pickle.load(f)

        prediction = loaded_model.predict(sample).item()
        confidence = loaded_model.predict_proba(sample)[0][0]


        result = {'malignant_status': prediction, 'confidence': confidence}

        return jsonify(result)
