#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:00:39 2022

@author: alex
"""

# Description: This script extracts ALL the articles from the Ynet breaking news

import requests
from bs4 import BeautifulSoup as soup


# Method Purpose: This method extracts the URLs from an HTML.

def get_content_links(url):
    page = requests.get(url)
    page_soup = soup(page.content, 'html.parser')
    containers = page_soup.find_all(class_="MultiArticleComponenta ArticleHeadlinesAuto englishSite withoutImage")
    containers_list = []
    links = []
    for ul in containers:
        containers_list.extend(ul.findAll('a'))
    for link in containers_list:
        links.append(link. get('href'))
    return links


# Method Purpose: This method extracts each article into a string.

def get_content_string(links):
    print(links[0])
    page = requests.get(links[0])
    page_soup = soup(page.content, 'html.parser')
    containers = page_soup.find_all(class_="layoutItem article-body-english")
    text = page_soup.get_text()
    text = " ".join(text.split())
    return text
    
    