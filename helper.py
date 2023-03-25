from Comment_scrapper import youtube_scrapper
from transformers import pipeline
import pandas as pd

def sentiment(video_url):
    with youtube_scrapper(video_url=video_url) as scrapper:
        comments, title = scrapper.yt_comments()
        sentiment_analysis = pipeline("sentiment-analysis")
        comment_analysis = sentiment_analysis(comments)
        df = pd.DataFrame.from_dict(comment_analysis)
        comments = pd.Series(comments)
        df["comments"] = comments
    return df,title


def plot_bar(df):
    pos, neg = (df["label"] == "POSITIVE").value_counts()
    labels = ["positive", "negative"]
    number = [pos, neg]
    return labels, number




