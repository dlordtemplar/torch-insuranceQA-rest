### Requirements

- flask
- spacy
- numpy
- torch
- pandas
- nltk
- gensim
- pyenchant (Can be replaced by pyhunspell)
- scikit_learn
- spacy (You will need to get the English model: "python -m spacy download en")

### Setup

[passage.py](passage.py) should automatically create a Whoosh directory when you start the project for the first time. Uses a pretrained model.

Do "flask run --port 5001" with the values below

    FLASK_APP=app
    FLASK_ENV=development

