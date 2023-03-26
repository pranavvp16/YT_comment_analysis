from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
VIDEO_URL = "https://www.youtube.com/watch?v=8l_fdwXazoc&t"

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--mute-audio")
options.add_argument("-no-sandbox")
options.add_argument("--disable-extension")
options.add_argument("-disable-dev-shm-usage")
os.environ['PATH'] += r"selenium_driver/chromedriver_mac64/chromedriver"
driver = webdriver.Chrome(options=options)
time.sleep(1)
driver.get(VIDEO_URL)
time.sleep(2)

#scroll down to load comments
#driver.execute_script("window.scrollBy(0,500)", "")

#last_height = driver.execute_script("return document.documentElement.scrollHeight")
#print(last_height)

while True:
    # Scroll down till "next load".
    driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")

    # Wait to load everything thus far.
    time.sleep(3)

    # Calculate new scroll height and compare with last scroll height.
    new_height = driver.execute_script("return document.documentElement.scrollHeight")
    #print(new_height)
    if new_height > 3000:
        break

#Scrap video title
video_title = driver.find_element(By.NAME, 'title').get_attribute('content')
comments = driver.find_elements(By.XPATH, '//*[@id="content-text"]')

# Extract comment text from each element
for comment in comments:
    print(comment.text)

print(video_title)
# Close the browser
driver.quit()



