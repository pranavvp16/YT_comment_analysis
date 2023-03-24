from Comment_scrapper import youtube_scrapper
from transformers import pipeline
import pandas as pd


def sentiment(video_url):
    with youtube_scrapper(video_url=video_url) as scrapper:
        comments = scrapper.yt_comments()
        comments = pd.Series(comments)
        sentiment_analysis = pipeline("sentiment-analysis")
        comment_analysis = sentiment_analysis(comments)
        df = pd.DataFrame.from_dict(comment_analysis)
        df["comments"] = comments
    return df
