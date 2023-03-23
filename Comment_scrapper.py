from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os
import numpy as np



class comment_scapper(webdriver.Chrome):
    """
    This is a youtube comment scrapper made with selenium to scrap comments given a URL
    Parameters
    video_url : (string)
    """
    def __init__(self,driver_path="r/selenium_driver/chromedriver_mac64/chromedriver",video_url="string"):
        self.driver_path = driver_path
        self.video_url = video_url
        os.environ['PATH'] += self.driver_path
        super(comment_scapper, self).__init__()

    def yt_comments(self,convert_to_csv=False):
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









