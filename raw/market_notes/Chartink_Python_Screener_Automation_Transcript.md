---
title: Video Transcript - Automating Chartink Screeners via Python & Web Scraping
source: Trade Invest YouTube Tutorial
date: 2026-10-18
tags:
  - raw-source
  - chartink
  - python
  - web-scraping
  - algo-screening
---

# Video Transcript: Automating Chartink Screeners via Python & Web Scraping

## Verbatim Transcript
Hello guys welcome back to another video of trade invest In today's video we are going to talk about how we can fetch the screener data in python and how we can do trading on it. We will talk about that in the next video. So without twisting the video, let's start the video. Before that if you want to watch the video then like the video and subscribe to the channel. Let's start this video. So guys here we go to the screener on the charting. And here we open a 100% accuracy scanner which is made by a brother.

And here we have a scan of the data which we can do. We take the intraday stocks and scan it. So here we have total 18 stocks which we can buy. So after that what we have to do here is you go here. After that you will get a url here. And here you will get a url. So as soon as you go to the inspect element here. So here we will click on the network tab. And as soon as you refresh it. So here you will get a process in the network tab. So in the process you will click on preview. In headers you will get this process.

And here we have another screener and process. So here you will get a url. We have to use this url. So as soon as you use the url here. This end point url. And you have to import request or beautiful sooc. Because this is what we will help you. To beautify your data. And we will fetch the data HTML content. We will convert that content to data. So here you get a response.get. With the help of request module. And this url is passed here. End point url. We are using this here. Same url screener. So as soon as we print it.

We will get the HTML content in the soup. We need meta from here. Meta content. So we need meta here. I have already written the code here. So I am showing you step by step. So here we have taken the soup pass. But we need csrf token. So we will take the csrf token. This is the meta data. And we have csrf token. You will get the csrf token. So I am printing csrf token here. In the meta we have given another query. The name of the csrf token. We need to copy the content. So here I am copying it.

And here we print it. So we will get csrf token. So here you will see csrf token. So what we will do with the csrf token. We will request the same data. Here we have made a request adder. Xcsrf token. So here you will see. Xcsrf token. So if you go down here. You will get it. Xcsrf token. You can see here. Our url is something else. Here the xcsrf token. This is the charting.screener.by. Entry data. There we have some other xcsrf token. Here you will get xcsrf token. You have to pass the csrf token in the referral screen.

As you pass the csrf token. You will get the request response. So the response post status. If it is 200. We will get the JSON data. So let's see what we get. So here we got the data. So what data we got. So here in scan condition. Like we have passed one more thing. In response.goat. Endpoint url. And the data we need is scan condition. Where will you get scan condition. So you will go to scan condition. In preview. Not in preview. You will get scan close. Let's copy this scan close. Guys we made a big mistake here.

[... Transcript continues explaining: copying scan_clause from Chrome Network tab -> handling JSON response -> converting to pandas DataFrame -> testing with NR7 scanner yielding 54 stocks in 0.90 seconds -> Selenium alternative using Chrome WebDriver].
