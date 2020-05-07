import warnings
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
warnings.filterwarnings('ignore')
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import Tokenizer

import pickle
model = load_model('model.h5')
with open('tokenizer.pkl', 'rb') as handle:
    tokenizer = pickle.load(handle)
POSITIVE = "POSITIVE"
NEGATIVE = "NEGATIVE"
NEUTRAL = "NEUTRAL"
SENTIMENT_THRESHOLDS = (0.4, 0.7)


def decode_sentiment(score, include_neutral=True):
    if include_neutral:        
        label = NEUTRAL
        if score <= SENTIMENT_THRESHOLDS[0]:
            label = NEGATIVE
        elif score >= SENTIMENT_THRESHOLDS[1]:
            label = POSITIVE

        return label
    else:
        return NEGATIVE if score < 0.5 else POSITIVE

def predict(text, include_neutral=True):
    x_test = pad_sequences(tokenizer.texts_to_sequences([text]), maxlen=300)
    score = model.predict([x_test])[0]
    label = decode_sentiment(score, include_neutral=include_neutral)
    return {"label": label, "score": float(score)}


# from textblob import TextBlob, Word, Blobber

# t = TextBlob(text)
# t.sentiment



