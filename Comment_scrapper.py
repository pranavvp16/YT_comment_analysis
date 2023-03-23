from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import numpy as np

options = webdriver.ChromeOptions
options.add_argument("--headless")
options.add_argument("--mute-audio")
options.add_argument("-no-sandbox")
options.add_argument("--disable-extension")
options.add_argument("-disable-dev-shm-usage")

class youtube_scapper(webdriver.Chrome(options=options)):
    """
        This is a youtube scrapper is made with selenium to scrap different elements
        on the youtube web-page given a URL
        Parameters
        video_url : (string)
    """
    def __init__(self,driver_path="r/selenium_driver/chromedriver_mac64/chromedriver",video_url="string"):
        self.driver_path = driver_path
        self.video_url = video_url
        os.environ['PATH'] += self.driver_path
        super(youtube_scapper, self).__init__()

    def yt_comments(self,convert_to_csv=False):
        """
            Scraps youtube comments
            Parameters:
                convert_to_csv = False (default)
                Set to True to get output in a form of .csv file
        """
        self.get(self.video_url)
        while True:
            self.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
            time.sleep(2)
            new_height = self.execute_script("return document.documentElement.scrollHeight")
            if new_height > 3000:
                break
        comments = self.find_elements(By.XPATH, '//*[@id="content-text"]')
        comments_list =[]
        for i in comments:
            comments_list.append(i.text)
        #return comments_list
        if convert_to_csv is True:
            np.savetxt("video_comments.csv",comment_list,delimiter=",",fmt='% s')
        else:
            return comments_list









