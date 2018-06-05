#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Use text editor to edit the script and type in valid Instagram username/password

from InstagramAPI import InstagramAPI
from bs4 import BeautifulSoup

# First get the populate hashtags
import wget

import requests
import json
import urllib.request
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
import random

InstagramAPI = InstagramAPI("botbait", "")
InstagramAPI.login()  # login

while True:


    url = 'https://api.ritekit.com/v1/search/trending?green=1&latin=1'
    r = requests.get(url)
    trending = json.loads(r.content);
    trending_tag_list = [];
    for tag in trending['tags']:
        trending_tag_list.append(tag['tag'])




    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument('--disable-gpu')  # Last I checked this was necessary.

    driver = webdriver.Chrome(chrome_options=chrome_options)
    taggg = random.choice(trending_tag_list)
    related_url = "https://hashtagify.me/hashtag/"+taggg.replace('#','')+"/"
    driver.get(related_url) #Browser goes to google.com
    driver.execute_script("window.scrollTo(0, 500);")
    driver.implicitly_wait(10) # seconds
    elems = driver.find_elements_by_css_selector("a.wordcloudlink")
    post_string = '#' + taggg

    for e in elems:
        post_string = post_string + ' ' + e.text

    # Get related
    #
    #
    #
    ig_url = "https://www.instagram.com/explore/tags/"+taggg.replace('#','')+"/"
    driver.get(ig_url) #Browser goes to google.com
    elems = driver.find_elements_by_css_selector("img")[11].get_attribute("src")
    driver.quit()

    urllib.request.urlretrieve(elems, "post.jpg")



    photo_path = './post.jpg'
    caption = post_string
    print(caption)
    InstagramAPI.uploadPhoto(photo_path, caption=caption)

    time.sleep(120)
