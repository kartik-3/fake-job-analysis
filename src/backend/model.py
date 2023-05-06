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

class NLPModel(object):

    class predictors(TransformerMixin):
        def transform(self, X, **transform_params):
            # Cleaning Text
            return [text.strip().lower() for text in X]

        def fit(self, X, y=None, **fit_params):
            return self

        def get_params(self, deep=True):
            return {}

    def __init__(self):
        """Simple NLP
        Attributes:
            clf: sklearn classifier model
            vectorizor: TFIDF vectorizer or similar
        """
        self.punctuations = string.punctuation
        self.stopwords = STOP_WORDS
        self.parser = English()

        self.data = self.read_pkl("./data_combined.pkl")
        self.X = self.data.text
        self.y = self.data.fraudulent
        self.X_train, self.X_test, self.Y_train, self.Y_test = train_test_split(self.data.text, self.data.fraudulent, test_size=0.3)

        self.clf = LogisticRegression(class_weight='balanced')
        self.tokenizer = self.tokenizer_fn
        self.vector = CountVectorizer(tokenizer=self.tokenizer, ngram_range=(1, 2))
        self.pipe = self.create_pipeline()
        self.vectorizer_fit(self.X_train, self.Y_train)
        self.pickle_vectorizer()
        self.pickle_clf()
        self.pickle_pipe()

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

    def create_pipeline(self):
        pipe = Pipeline([("cleaner", self.predictors()),
                         ('vectorizer', self.vector),
                         ('classifier', self.clf)])
        
        return pipe

    def vectorizer_fit(self, X_train, Y_train):
        """Fits a TFIDF vectorizer to the text
        """
        self.pipe.fit(X_train, Y_train)

    def read_pkl(self, file):
        return pd.read_pickle(file)
    
    def vectorizer_transform(self, X):
        """Transform the text data to a sparse TFIDF matrix
        """
        X_transformed = self.vector.transform(X)
        return X_transformed

    def train(self, X, y):
        """Trains the classifier to associate the label with the sparse matrix
        """
        # X_train, X_test, y_train, y_test = train_test_split(X, y)
        self.pipe.fit(X, y)

    def predict_proba(self, X):
        """Returns probability for the binary class '1' in a numpy array
        """
        y_proba = self.clf.predict_proba(X)
        return y_proba[:, 1]

    def predict(self, X):
        """Returns the predicted class in an array
        """
        y_pred = self.pipe.predict(X)
        return y_pred

    def pickle_vectorizer(self, path='./models/CountVectorizer.pkl'):
        """Saves the trained vectorizer for future use.
        """
        with open(path, 'wb') as f:
            pickle.dump(self.vector, f)
            print("Pickled vectorizer at {}".format(path))

    def pickle_clf(self, path='./models/LogisticClassifier.pkl'):
        """Saves the trained classifier for future use.
        """
        with open(path, 'wb') as f:
            pickle.dump(self.clf, f)
            print("Pickled classifier at {}".format(path))


    def pickle_pipe(self, path='./models/pipe.pkl'):
        """Saves the trained classifier for future use.
        """
        with open(path, 'wb') as f:
            pickle.dump(self.pipe, f)
            print("Pickled pipe at {}".format(path))

    # def plot_roc(self, X, y, size_x, size_y):
    #     """Plot the ROC curve for X_test and y_test.
    #     """
    #     plot_roc(self.clf, X, y, size_x, size_y)
