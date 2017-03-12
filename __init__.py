# -*- coding: utf-8 -*-
import json
import subprocess

from adapt.intent import IntentBuilder
from os.path import dirname
import youtube_dl
import urllib
import urllib2
from bs4 import BeautifulSoup

from mycroft.skills.core import MycroftSkill

__author__ = 'augustnmonteiro'


class YoutubeSkill(MycroftSkill):
    def __init__(self):
        super(YoutubeSkill, self).__init__(name="YoutubeSkill")
        self.process = None

    def initialize(self):
        self.load_data_files(dirname(__file__))

        youtube = IntentBuilder("YoutubeKeyword"). \
            require("YoutubeKeyword").build()
        self.register_intent(youtube, self.youtube)


    def search(self, text):
        query = urllib.quote(text)
        url = "https://www.youtube.com/results?search_query=" + query
        response = urllib2.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html)
        for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
	            if not vid['href'].startswith(u"https://googleads.g.doubleclick.net/‌​") and not vid['href'].startswith(u"/user")  and not vid['href'].startswith(u"/channel") :
                      return "http://www.youtube.com/"+vid['href']

    def youtube(self, message):
        self.stop()
        utterance = message.data.get('utterance').lower()
        utterance = utterance.replace(
            message.data.get('YoutubeKeyword'), '')
        vid = self.search(utterance)
        self.process = subprocess.Popen(["mpv",vid] )

    def stop(self):
        if self.process:
            self.process.terminate()
            self.process.wait()
        pass


def create_skill():
    return YoutubeSkill()
