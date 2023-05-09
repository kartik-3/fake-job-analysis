#imports
import pickle
from spacy.lang.en.stop_words import STOP_WORDS
from spacy.lang.en import English
import string
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.base import TransformerMixin
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

#Creating our class for our model
class NLPModel(object):

    # predictors class to transform and fit our model
    class predictors(TransformerMixin):
        def transform(self, X, **transform_params):
            # Cleaning Text
            return [text.strip().lower() for text in X]

        def fit(self, X, y=None, **fit_params):
            return self

        def get_params(self, deep=True):
            return {}

    # constructor to initialize the object parameters
    def __init__(self):
        # creating variables for punctutations, stopwords, parser
        self.punctuations = string.punctuation
        self.stopwords = STOP_WORDS
        self.parser = English()

        # reading data from pickle file
        self.data = self.read_pkl("./data_combined.pkl")
        self.X = self.data.text
        self.y = self.data.fraudulent
        #splitting data into training and test
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.data.text, self.data.fraudulent, test_size=0.3)

        # creating our Logistic Regression classifier
        self.clf = LogisticRegression(class_weight='balanced')
        # tokenizing
        self.tokenizer = self.tokenizer_fn
        #creating vector using CountVectorizer
        self.vector = CountVectorizer(tokenizer=self.tokenizer, ngram_range=(1, 2))
        #creating pipe
        self.pipe = self.create_pipeline()
        #fitting pur model
        self.vectorizer_fit(self.X_train, self.Y_train)
        #creating pickle files
        self.pickle_vectorizer()
        self.pickle_clf()
        self.pickle_pipe()

    #function to tokenize our data
    def tokenizer_fn(self, sentence):
        # Creating our token object
        tokens = self.parser(sentence)
        # Lemmatizing each token and converting each token into lowercase
        tokens = [word.lower_ for word in tokens]
        # Removing stop words
        tokens = [
            word for word in tokens if word not in self.stopwords and word not in self.punctuations]
        # return a preprocessed list of tokens
        return tokens

    #function to create the pipeline
    def create_pipeline(self):
        return Pipeline([
            ("cleaner", self.predictors()),
            ('vectorizer', self.vector),
            ('classifier', self.clf)]
            )

    #Fits a count vectorizer to the text
    def vectorizer_fit(self, X_train, Y_train):
        self.pipe.fit(X_train, Y_train)

    #read pickle file
    def read_pkl(self, file):
        return pd.read_pickle(file)

    #Transform the text data to a sparse matrix
    def vectorizer_transform(self, X):
        X_transformed = self.vector.transform(X)
        return X_transformed

    #"Trains the classifier to associate the label with the sparse matrix
    def train(self, X, y):
        """Trains the classifier to associate the label with the sparse matrix
        """
        # X_train, X_test, y_train, y_test = train_test_split(X, y)
        self.pipe.fit(X, y)

    #Returns probability for the binary class '1' in a numpy array
    def predict_proba(self, X):
        y_proba = self.pipe.predict_proba(X)
        return y_proba[:, 1]

    #Returns the predicted class in an array
    def predict(self, X):
        y_pred = self.pipe.predict(X)
        return y_pred

    #Saves the trained vectorizer for future use.
    def pickle_vectorizer(self, path='./models/CountVectorizer.pkl'):
        with open(path, 'wb') as f:
            pickle.dump(self.vector, f)
            print("Pickled vectorizer at {}".format(path))

    #Saves the trained classifier for future use.
    def pickle_clf(self, path='./models/LogisticClassifier.pkl'):
        with open(path, 'wb') as f:
            pickle.dump(self.clf, f)
            print("Pickled classifier at {}".format(path))

    #Saves the trained pipe for future use.
    def pickle_pipe(self, path='./models/pipe.pkl'):
        with open(path, 'wb') as f:
            pickle.dump(self.pipe, f)
            print("Pickled pipe at {}".format(path))
