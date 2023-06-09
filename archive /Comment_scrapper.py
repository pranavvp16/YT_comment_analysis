from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import numpy as np

class youtube_scrapper(webdriver.Chrome):
    """
        This is a youtube scrapper is made with selenium to scrap different elements
        on the youtube web-page given a URL
        Parameters
        video_url : (string)
        teardown : bool
    """
    def __init__(self,video_url="string",teardown=True):
        self.teardown = teardown
        self.video_url = video_url
        super(youtube_scrapper, self).__init__()
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Executing teardown")
        if self.teardown:
            self.quit()
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
        video_title = self.find_element(By.NAME, 'title').get_attribute('content')
        comments_list =[]
        for i in comments:
            comments_list.append(i.text)
        #return comments_list
        if convert_to_csv is True:
            np.savetxt("video_comments.csv",comment_list,delimiter=",",fmt='% s')
        else:
            return comments_list,video_title











