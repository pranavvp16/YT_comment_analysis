import streamlit as st
from helper import sentiment

st.sidebar.title("Comment Analytics")
video_url = st.sidebar.text_input("Enter Video URL of the video for analysis")
if "https://youtu.be" not in video_url:
    st.sidebar.write("Enter video URL")
else:
    sentiment(video_url)