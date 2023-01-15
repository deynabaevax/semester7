import joblib
import re
from sklearn.neural_network import MLPClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
import streamlit as st
import streamlit.components.v1 as components
from lime.lime_text import LimeTextExplainer


st.set_page_config(
    page_title="Text Classification",
    page_icon="🧾",
)


st.sidebar.header("Text Classification app for detecting spam messages. ")
st.write("# Spam Detection")
message_text = st.text_input("Enter a message for spam evaluation")


def preprocessor(text):
    text = re.sub('<[^>]*>', '', text)  # Effectively removes HTML markup tags
    emoticons = re.findall('(?::|;|=)(?:-)?(?:\)|\(|D|P)', text)
    text = re.sub('[\W]+', ' ', text.lower()) + \
        ' '.join(emoticons).replace('-', '')
    return text


model = joblib.load('spam_classifier.joblib')


def classify_message(model, message):

    label = model.predict([message])[0]
    spam_prob = model.predict_proba([message])

    return {'label': label, 'spam_probability': spam_prob[0][1]}


if message_text != '':

    result = classify_message(model, message_text)

    st.write(result)

    explain_pred = st.button('Explain Predictions')

    if explain_pred:
        with st.spinner('Generating explanations'):
            class_names = ['ham', 'spam']
            explainer = LimeTextExplainer(class_names=class_names)
            exp = explainer.explain_instance(message_text,
                                             model.predict_proba, num_features=10)
            components.html(exp.as_html(), height=800)


def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
    background-image: url("data:design/png;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
