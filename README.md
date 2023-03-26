# Youtube Comment Analystics
#### Harnessing Natural Language Processing for valuable insights

In today's age content creator face with the challenge of understanding there audience 
feedback to improve there content quality. Majority of these 
feedbacks are found in comments section in the form of comments. It may get hectic to analyse these comments manaually.
This project aims to harness the power of Data Analysis and NLP to give valuable insights to the creator.


**Working** : This app uses the Selenium to scrap the youtube comments given URL of the video. This comments are passed to Hugging Face NLP transformer pipeline to perform sentiment analysis on the comments. The analysis helps the app to generate graphs with Matplotlib and give insigths through graphs

**Tools**
- Selenium
- Streamlit
- Pandas
- Hugging Face
- Matplotlib