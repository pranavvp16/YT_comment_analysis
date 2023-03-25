import streamlit as st
from helper import sentiment
import matplotlib.pyplot as plt


@st.cache_data()
def dataframe(url):
    data, video_title = sentiment(video_url)
    return data, video_title


st.sidebar.title("Comment Analytics")
video_url = st.sidebar.text_input("Enter Video URL of the video for analysis")

if "https://youtu.be" not in video_url:
    st.sidebar.write("Enter video URL")
else:
    df, title = dataframe(video_url)
    st.title(title)
    filter_sentiment = st.sidebar.selectbox("Filter", ["Overall", "POSITIVE", "NEGATIVE"])
    if filter_sentiment != "Overall":
        filtered_df = df[df["label"] == filter_sentiment]
        st.dataframe(filtered_df)
    else:
        st.dataframe(df)


