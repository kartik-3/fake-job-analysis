from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
from model import NLPModel
import re

app = Flask(__name__)
api = Api(app)
# create new model object
model = NLPModel()
# load trained classifier
clf_path = './models/LogisticClassifier.pkl'
with open(clf_path, 'rb') as f:
    model.clf = pickle.load(f)

pipe_path = './models/LogisticClassifier.pkl'
with open(pipe_path, 'rb') as f:
    model.pipe = pickle.load(f)

# load trained vectorizer
vec_path = './models/CountVectorizer.pkl'
with open(vec_path, 'rb') as f:
    model.vector = pickle.load(f)


# argument parsing
parser = reqparse.RequestParser()
parser.add_argument('query')


class PredictJob(Resource):
    def get(self):
        # use parser and find the user's query
        args = parser.parse_args()
        user_query = args['query']
        user_query = clean_text(user_query)

        # vectorize the user's query and make a prediction
        uq_vectorized = model.vectorizer_transform(np.array([user_query]))
        prediction = model.predict(uq_vectorized)
        pred_proba = model.predict_proba(uq_vectorized)
        # Output either 'Negative' or 'Positive' along with the score
        if prediction == 0:
            pred_text = 'Negative'
        else:
            pred_text = 'Positive'

        # round the predict proba value and set to new variable
        confidence = round(pred_proba[0], 3)

        # create JSON object
        output = {'prediction': pred_text, 'confidence': confidence}

        return output


def clean_text(text):
    text = re.sub('[^A-Za-z0-9]+', ' ', text)
    # Remove extra white space characters from start and end of string columns
    text = text.strip()
    # Replace uppercase characters with lowercase characters
    text = text.lower()
    return text


# Setup the Api resource routing here
# Route the URL to the resource
api.add_resource(PredictJob, '/')


if __name__ == '__main__':
    app.run(port="5050", debug=True)
