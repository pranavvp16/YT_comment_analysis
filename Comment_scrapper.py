from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

class Comment_scapper(webdriver.Chrome):
    """
    This is a youtube comment scrapper made with selenium to scrap comments given a URL
    Parameters
    video_url : (string)
    """
    def __init__(self,driver_path="r/selenium_driver/chromedriver_mac64/chromedriver",video_url="string"):
        self.driver_path = driver_path
        self.video_url = video_url
        super(Comment_scapper, self).__init__()

    def yt_page(self):
        self.get(self.video_url)

