from Comment_scrapper import youtube_scrapper
from transformers import pipeline

scapper = youtube_scrapper(video_url="https://youtu.be/rq8cL2XMM5M")
comments = scapper.yt_comments()
analysis = pipeline(comments)
for i in analysis:
    print(analysis)
