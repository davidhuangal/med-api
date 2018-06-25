from flask import Flask
from flask_restful import Api
from resources.Hello import Hello
from resources.BreastCancer import Prediction

app = Flask(__name__)
api = Api(app)

api.add_resource(Hello, '/api/hello')
api.add_resource(Prediction, '/api/prediction')

if __name__ == '__main__':
    app.run(port=3000)
