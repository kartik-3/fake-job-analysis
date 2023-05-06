from flask import Flask, jsonify, request
# from flask_cors import CORS
# import urllib
import json
# import config
import os 
# import re
app = Flask(__name__)
# CORS(app)
import re


@app.route('/predict', methods = ['POST'])
def predict_job():
    # print(request, request.get_json())
    js=request.get_json()
    # print(js)
    qtext = str(js['text'])
    text = clean_text(qtext)
    print(text)
    response = {
        "response": "okay",
        "text": text
    }
    return jsonify(response)

@app.route('/', methods = ['GET'])
def get_job():
    return jsonify({"okay": "okay"})

def clean_text(text):
  text = re.sub('[^A-Za-z0-9]+', ' ', text)
  #Remove extra white space characters from start and end of string columns
  text = text.strip()
  #Replace uppercase characters with lowercase characters
  text = text.lower()
  return text

if __name__ == "__main__":
    # if os.path.exists('./backend'): os.chdir('./backend')
    app.run(host="0.0.0.0")