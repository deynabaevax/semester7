import streamlit as st
import pandas as pd
import numpy as np
# similarity
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import sent_tokenize
from sentence_transformers import SentenceTransformer
from PIL import Image
import tensorflow_hub as hub
import functions


def recommend_episodes():
    combined_df = pd.read_csv('../datasets/combined_df.csv')

    global df
    df = pd.read_csv('../datasets/summary_results.csv')
    df = df[['summary', 'label']]
    df = df.merge(combined_df, left_on='summary', right_on='Summary')
    df = df[['summary', 'label', 'Title', 'Name']]

    global input
    form = st.form(key='nlpForm')
    input = form.text_area('Enter your text here:')
    input = input.reshape(-1, 1)

    global emotion
    emotion = st.text_input('Emotion', 'enter your emotion here')

    with st.expander(label='Click here, to find the available emotions.'):
        st.write("""
                    'anger', 'neutral', 'fear', 'sadness', 'joy', 'disgust','surprise'
                    """)

    #recommend = st.button('Recommend!')
    submit = form.form_submit_button('Surprise me')
    if submit:
        st.success(
            "Fetching the episodes for you! Sit back, relax and grab a coffee!!☕")
        doc = functions.get_episodes_per_emotion(emotion)

        sbert_model = SentenceTransformer('bert-base-nli-mean-tokens')
        predicted_episode = functions.process_bert_similarity(
            sbert_model, input, doc)
        # show = functions.output(predicted_episode)
        st.write(f'Recommended Episode specially for you: {predicted_episode}')

        st.markdown("[![Foo](https://play-lh.googleusercontent.com/TBRwjS_qfJCSj1m7zZB93FnpJM5fSpMA_wUlFDLxWAb45T9RmwBvQd5cWR5viJJOhkI=s48-rw)](https://www.netflix.com/)")
        st.markdown("[![Foo](https://reviewed-com-res.cloudinary.com/image/fetch/s--87edWEK1--/b_white,c_limit,cs_srgb,f_auto,fl_progressive.strip_profile,g_center,q_auto,w_100/https://reviewed-production.s3.amazonaws.com/1591287416567/Hulu_Logo.jpg)](https://www.hulu.com/)")
        st.markdown("[![Foo](https://play-lh.googleusercontent.com/ELLR6rcIP_mr6pB4kX9QhBKF-najkWHfb8RqceX4CBsyel3o_W9DoGas7WfPgfiIsQ=w100-h480-rw)](https://www.hbo.com/)")
