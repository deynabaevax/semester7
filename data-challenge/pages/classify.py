from bert_sklearn import (BertClassifier,
                          load_model)
from textblob import TextBlob

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import warnings
import time

warnings.filterwarnings('ignore')


'''
st.balloons
'''


def classify():
    st.title("Algo Show")
    st.write(
        "Find something interesting to watch. 😃")

    global data
    data = pd.read_csv("../datasets/summary_results.csv")

    data = data.loc[:, ['summary', 'pred', 'label']]

    text = st.text_input("Enter your text:")
    if st.button('Predict'):
        model = load_model("../model/data_challenge_model.bin")
        predictions = model.predict([text])
        emotion = predictions[0]
        emotion_label = {0: 'anger', 1: 'neutral', 2: 'fear',
                         3: 'sadness', 4: 'joy', 5: 'disgust', 6: 'surprise'}
        label = emotion_label[emotion]
        st.success("Your predicted sentiment is: " + label)
        if label == 'joy' or label == 'surprise':
            st.balloons()
