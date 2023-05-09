## This file is NOT used. Just for testing purposes

# imports
from flask import Flask, jsonify, request
app = Flask(__name__)
import re

# POST route to test APIs
@app.route('/predict', methods = ['POST'])
def predict_job():
    js=request.get_json()
    qtext = str(js['text'])
    text = clean_text(qtext)
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