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

## DISCLAIMER !!
The words and other con­tent pro­vided in this project, and in any linked mate­ri­als, are not intended and should not be con­strued as med­ical advice. If the reader or any other per­son has a med­ical con­cern, he or she should con­sult with an appropriately-licensed physi­cian or other health care worker.

Never dis­re­gard pro­fes­sional med­ical advice or delay in seek­ing it because of some­thing you garnered from this project or in any linked materials. If you think you may have a med­ical emer­gency, call your doc­tor immediately.

The views expressed on this project have no rela­tion to those of any academic, hospital, practice or other insti­tu­tion with which the authors are  affiliated.
