import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk import sent_tokenize
import tensorflow_hub as hub
import streamlit as st
import similar
from PIL import Image


import nltk
nltk.download('punkt')


def get_episodes_per_emotion(emotion):
    global df
    df = pd.read_csv('../datasets/summary_results.csv')
    df = df[['summary', 'label']]

    combined_df = pd.read_csv('../datasets/combined_df.csv')

    df = df.merge(combined_df, left_on='summary', right_on='Summary')
    df = df[['summary', 'label', 'Title', 'Name']]
    new_df = df[df['label'] == emotion]
    new_df = new_df['summary'][:10]
    doc = new_df.values.tolist()

    return doc


def process_bert_similarity(model, base_document, documents):
    # This will download and load the pre-trained model offered by UKPLab.

    # Although it is not explicitly stated in the official document of sentence transformer, the original BERT is meant for a shorter sentence. We will feed the model by sentences instead of the whole documents.
    sentences = sent_tokenize(base_document)
    base_embeddings_sentences = model.encode(sentences)
    base_embeddings = np.mean(np.array(base_embeddings_sentences), axis=0)

    vectors = []
    for i, document in enumerate(documents):

        sentences = sent_tokenize(document)
        embeddings_sentences = model.encode(sentences)
        embeddings = np.mean(np.array(embeddings_sentences), axis=0)

        vectors.append(embeddings)

        print("making vector at index:", i)

    scores = cosine_similarity([base_embeddings], vectors).flatten()

    highest_score = 0
    highest_score_index = 0
    for i, score in enumerate(scores):
        if highest_score < score:
            highest_score = score
            highest_score_index = i

    most_similar_document = documents[highest_score_index]
    return most_similar_document
    #st.write("Most similar document by BERT with the score:", most_similar_document, highest_score)


def output(sentence):
    new = df[df['summary'] == sentence]
    output = new.loc[:, ["Name", "Title", "summary"]]
    if output['Name'].eq('Games of Throne').any():
        image = Image.open('../images/game_of_thrones.jpg')
    if output['Name'].eq('Big Bang Theory').any():
        image = Image.open('../images/bigbangtheory.jpg')

    if output['Name'].eq('Breaking Bad').any():
        image = Image.open('../images/breaking_bad.jpg')

    if output['Name'].eq('Friends').any():
        image = Image.open('../images/friends.jpg')

    if output['Name'].eq('How I met your mother').any():
        image = Image.open('../images/how_imetyour.jpg')

    if output['Name'].eq('Modern Family').any():
        image = Image.open('../images/modern_family.jpg')

    if output['Name'].eq('The Office').any():
        image = Image.open('../images/theoffice.jpg')

    return output, st.image(image, width=120), st.write(f'Episode Name:', output['Title'].values.tolist()[0])
