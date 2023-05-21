#from Comment_scrapper import youtube_scrapper
import pandas
from transformers import pipeline
from wordcloud import WordCloud
import pandas as pd
from youtube_api import YoutubeAPI
import pickle as pkl
from keys import api_key
import re

def extract_video_id(video_url):
    regex_pattern = r"(?:v=|\/videos\/|embed\/|youtu.be\/|\/v\/|\/e\/|u\/\w+\/|embed\/|v=|e\/|u\/\w+\/|watch\?v=|&v=|\?v=)([^#\&\?]*)(?:[\?\&\#].*|$)"
    match = re.search(regex_pattern, video_url)
    if match:
        return match.group(1)
    else:
        return None

def sentiment(video_id):
    comments, video_title, subscriber_count, channel_name = YoutubeAPI(api_key, video_id)

    comment_classifier = pkl.load(open("Pickle_file/question_classifier.pkl", 'rb'))
    vectorizer = pkl.load(open("Pickle_file/text_vectorizer.pkl", 'rb'))

    interrogative_comments = []
    feedback_comments = []
    for comment in comments:
        label = comment_classifier.predict(vectorizer.transform([comment]))
        if label in ["whQuestion", "ynQuestion"]:
            question_dict = {}
            question_dict['label'] = 'QUESTION'
            question_dict['comment'] = comment
            interrogative_comments.append(question_dict)
        else:
            feedback_comments.append(comment)

    sentiment_analysis = pipeline("sentiment-analysis")
    comment_analysis = sentiment_analysis(feedback_comments)
    df_feedback = pandas.DataFrame.from_dict(comment_analysis)
    feedback_comments = pd.Series(feedback_comments)
    df_feedback["comments"] = feedback_comments
    df_question = pd.DataFrame.from_dict(interrogative_comments)
    return df_question,df_feedback,video_title, channel_name, subscriber_count


def plot_bar(df):
    pos, neg = (df["label"] == "POSITIVE").value_counts()
    labels = ["positive", "negative"]
    number = [pos, neg]
    return labels, number


def wc_gen(df):
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color="white")
    df_wc = wc.generate(df['comments'].str.cat(sep=" "))
    return df_wc



