import streamlit as st
import helper
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

    fig, ax = plt.subplots()
    fig1, ax1 = plt.subplots()
    col1, col2 = st.columns(2)
    label, numbers = helper.plot_bar(df)
    with col1:
        ax.bar(label, numbers, color="red")
        st.pyplot(fig)
    with col2:
        ax1.pie(numbers,labels=label, autopct='%1.1f%%', startangle=90,colors=['white', 'red'],
                wedgeprops={'edgecolor': 'black', 'linewidth': 2})
        st.pyplot(fig1)

    df_wc = helper.wc_gen(df)
    fig, ax = plt.subplots()
    ax.imshow(df_wc)
    st.pyplot(fig)







