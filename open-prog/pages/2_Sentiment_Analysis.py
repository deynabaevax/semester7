from string import punctuation
import regex as re
import streamlit as st
from textblob import TextBlob
import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="🫠",
)

st.sidebar.header("Sentiment Analysis")
# creating a dataframe


def convert_to_df(sentiment):
    sentiment_dict = {'polarity': sentiment.polarity,
                      'subjectivity': sentiment.subjectivity}
    sentiment_df = pd.DataFrame(
        sentiment_dict.items(), columns=['metric', 'value'])
    return sentiment_df

# analyzing the sentiment


def analyze_token_sentiment(docx):
    analyzer = SentimentIntensityAnalyzer()
    pos_list = []
    neg_list = []
    neu_list = []
    for i in docx.split():
        res = analyzer.polarity_scores(i)['compound']
        if res > 0.1:
            pos_list.append(i)
            pos_list.append(res)

        elif res <= -0.1:
            neg_list.append(i)
            neg_list.append(res)
        else:
            neu_list.append(i)

    result = {'positives': pos_list,
              'negatives': neg_list, 'neutral': neu_list}
    return result


def main():
    st.title("Sentiment Analysis")
    st.write(
        "Check your input's sentiment analysis. :smiley:")

    form = st.form(key='nlpForm')
    user_input = form.text_area('Enter your text here:')
    submit = form.form_submit_button('Make prediction')

    # layout
    col1, col2 = st.columns(2)

    if submit:
        with col1:
            st.info("Results")
            sentiment = TextBlob(user_input).sentiment
            st.write(sentiment)

            # Emoji
            if sentiment.polarity > 0:
                st.markdown("Sentiment: Positive :smiley: ")
            elif sentiment.polarity < 0:
                st.markdown("Sentiment: Negative :angry: ")
            else:
                st.markdown("Sentiment: Neutral 😐 ")

                # Dataframe
                result_df = convert_to_df(sentiment)
                st.dataframe(result_df)

                # Visualization
                # c = alt.Chart(result_df).mark_bar().encode(
                #     x='metric',
                #     y='value',
                #     color='metric')

            with col2:
                st.info("Token Sentiment")

                token_sentiments = analyze_token_sentiment(user_input)
                st.write(token_sentiments)


if __name__ == '__main__':
    main()
