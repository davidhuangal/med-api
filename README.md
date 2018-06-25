# med-api
A RESTful API for medical applications of machine learning.

## Installation Instructions

1. Clone the repository wherever you'd like.
2. Create a virtual environment in the 'med-api' directory. For example:

```
python3 -m virtualenv med-api
```

And then in the med-api directory:

```
source bin/activate
```

3. In the med-api directory, install the requirements with pip:

```
pip3 install -r requirements.txt
```

4. Run app.py

```
python3 app.py
```

The app should run. You can test it out with the two test json files. Currently the only feature is giving a prediction for breast cancer:

```
curl -X POST -H "Content-Type: application/json" -d @test.json http://localhost:3000/api/breast-cancer/prediction

{
  "confidence": 0.9999998999999902,
  "malignant_status": 0
}
```

```
curl -X POST -H "Content-Type: application/json" -d @test2.json http://localhost:3000/api/breast-cancer/prediction

{
  "confidence": 0.9999994043330815,
  "malignant_status": 0
}

```


## TODO:
* Implementing more classification features.
* Add support for databases.
