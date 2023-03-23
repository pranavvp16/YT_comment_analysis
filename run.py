from Comment_scrapper import comment_scapper

scapper = comment_scapper(video_url="https://youtu.be/rq8cL2XMM5M")
comments = scapper.yt_comments()

