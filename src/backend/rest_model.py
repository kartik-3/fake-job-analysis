from flask import Flask, jsonify, request
from flask_cors import CORS, cross_origin
from flask_restful import reqparse, abort, Api, Resource
import pickle
import numpy as np
from model import NLPModel
import re
import pandas as pd
import json

app = Flask(__name__)
# CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "http://localhost:8080"}})

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
parser.add_argument('job_title')
parser.add_argument('job_description')
parser.add_argument('job_requirements')
parser.add_argument('job_benefits')
parser.add_argument('company_profile')


class NpEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.integer):
            return int(obj)
        if isinstance(obj, np.floating):
            return float(obj)
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return super(NpEncoder, self).default(obj)

# Your codes ....
# json.dumps(data, cls=NpEncoder)


class PredictJob(Resource):
    def post(self):
        # use parser and find the user's query
        args = parser.parse_args()
        job_title = args['job_title']
        job_description = args['job_description']
        job_requirements = args['job_requirements']
        job_benefits = args['job_benefits']
        company_profile = args['company_profile']
        user_query = job_title + " " + company_profile + " " + \
            job_description + " " + job_requirements + " " + job_benefits
        user_query = clean_text(user_query)

        # vectorize the user's query and make a prediction
        uq_vectorized = model.vectorizer_transform(np.array([user_query]))
        prediction = model.predict(uq_vectorized)
        pred_proba = model.predict_proba(uq_vectorized)
        # Output either 'Negative' or 'Positive' along with the score
        print(prediction)
        if prediction == 0:
            pred_text = 'Negative'
        else:
            pred_text = 'Positive'

        if len(user_query) < 50:
            pred_text = "Neutral"

        # round the predict proba value and set to new variable
        confidence = round(pred_proba[0], 3)
        print(confidence)
        # create JSON object
        output = jsonify({'prediction': pred_text, 'confidence': confidence})

        return output

    def get(self):
        data = pd.read_pickle("./data.pkl")
        counts = {}
        data_by_id = {}

        all_cols = list(data.columns.values)
        all_cols = all_cols[:-2]

        data_by_cols = data.to_dict()
        data_by_cols.pop('salary_max', None)
        data_by_cols.pop('salary_min', None)

        for col in all_cols:
            counts[col] = data[col].value_counts()

        not_provided_counts, provided_counts, total = {}, {}, 12372
        for col in counts:
            if 'not provided' in counts[col]:
                not_provided_counts[col] = counts[col]["not provided"]
                provided_counts[col] = total - counts[col]["not provided"]

        for id in data_by_cols['job_id']:
            new_data = {}
            for col in all_cols:
                new_data[col] = data_by_cols[col][id]
                data_by_id[id+1] = new_data

        output = json.dumps({'not_provided_counts': not_provided_counts, 'provided_counts': provided_counts,
                            'data_by_cols': dict(data_by_cols), 'data_by_id': dict(data_by_id)}, cls=NpEncoder)
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
api.add_resource(PredictJob, '/predict')

if __name__ == '__main__':
    app.run(port="5000", debug=True)
