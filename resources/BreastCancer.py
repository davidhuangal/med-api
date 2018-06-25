from flask import request
from flask_restful import Resource
import pickle
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

class Prediction(Resource):

    def post(self):

        sample = request.json

        radius_mean = sample['radius_mean']
        texture_mean =	sample['texture_mean']
        perimeter_mean = sample['perimeter_mean']
        area_mean =	sample['area_mean']
        smoothness_mean = sample['smoothness_mean']
        compactness_mean =sample['compactness_mean']
        concavity_mean = sample['concavity_mean']
        concave_points_mean = sample['concave_points_mean']
        symmetry_mean = sample['symmetry_mean']
        fractal_dimension_mean = sample['fractal_dimension_mean']
        radius_standard_error = sample['radius_standard_error']
        texture_standard_error = sample['texture_standard_error']
        perimeter_standard_error = sample['perimeter_standard_error']
        area_standard_error = sample['area_standard_error']
        smoothness_standard_error = sample['smoothness_standard_error']
        compactness_standard_error = sample['compactness_standard_error']
        concavity_standard_error = sample['concavity_standard_error']
        concave_points_standard_error = sample['concave_points_standard_error']
        symmetry_standard_error = sample['symmetry_standard_error']
        fractal_dimension_standard_error = sample['fractal_dimension_standard_error']
        radius_worst = sample['radius_worst']
        texture_worst = sample['texture_worst']
        perimeter_worst = sample['perimeter_worst']
        area_worst = sample['area_worst']
        smoothness_worst = sample['smoothness_worst']
        compactness_worst = sample['compactness_worst']
        concavity_worst = sample['concavity_worst']
        concave_points_worst = sample['concave_points_worst']
        symmetry_worst = sample['symmetry_worst']
        fractal_dimension_worst = sample['fractal_dimension_worst']

        with open('./models/breast_cancer_model.sav', 'rb') as f:
            loaded_model = pickle.load(f)

        prediction = loaded_model.predict(sample)
        confidence = loaded_model.predict_proba(sample)[0][1]

        return {'malignant_status': prediction, 'confidence': confidence}
