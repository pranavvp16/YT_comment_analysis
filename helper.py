#from Comment_scrapper import youtube_scrapper
import pandas
from transformers import pipeline
from wordcloud import WordCloud
import pandas as pd
from youtube_api import YoutubeAPI
import pickle as pkl
from keys import api_key
from langdetect import detect
from deep_translator import GoogleTranslator

def translate_comments(list_comment, target_language):
    comments_translated = []
    for comment in list_comment:
        print(comment)
        try:
            if detect(comment)==target_language:
             comments_translated.append(comment)
        
            else:
                translated = GoogleTranslator(source='auto', target='en').translate(comment)
                comments_translated.append(translated)
        except Exception:
            pass
    return comments_translated



def sentiment(video_url):
    comments, video_title, subscriber_count, channel_name = YoutubeAPI(api_key, video_url)

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

    translated_comments = translate_comments(feedback_comments,'en')
    model = pipeline(model="distilbert-base-uncased-finetuned-sst-2-english")
    comment_analysis = model(translated_comments)
    df_feedback = pandas.DataFrame.from_dict(comment_analysis)
    feedback_comments = pd.Series(feedback_comments)
    df_feedback["comments"] = feedback_comments
    df_question = pd.DataFrame.from_dict(interrogative_comments)
    return df_question,df_feedback,video_title, channel_name, subscriber_count


def plot_bar(df):
    try:
        pos, neg = (df["label"]).value_counts()
        labels = ["positive", "negative"]
        number = [pos, neg]
    except Exception:
        label = (df["label"]).value_counts()
        labels = ["positive","negative"]
        number = [label,0]
    return labels, number


def wc_gen(df):
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color="white")
    df_wc = wc.generate(df['comments'].str.cat(sep=" "))
    return df_wc



