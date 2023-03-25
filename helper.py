from Comment_scrapper import youtube_scrapper
from transformers import pipeline
from wordcloud import WordCloud
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


def wc_gen(df):
    wc = WordCloud(width=500, height=500, min_font_size=10, background_color="white")
    df_wc = wc.generate(df['comments'].str.cat(sep=" "))
    return df_wc



