#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:22:13 2022

@author: alex
"""

import requests
from bs4 import BeautifulSoup as soup
from newspaper import Article


my_url = "https://www.ynetnews.com/category/3089"


# Method Purpose: This method extracts a content dictionary from an HTML outline of the NY Times Tech Section.
# Parameter: The URL of the NY Times Tech Section.
# Steps (How it Works):
# 1. Gets a script of all the HTML on the page.
# 2. Gets an article list - a snippet of the HTML outline including all of the articles.
# 3. The content string is the first element of this list.
# 4. The index of the "itemListElement" is used to extract a library of all the article hyperlinks and metadata.
# 5. A substring of the content string is taken to remove the "itemListElement" from the string.

def get_content_links(url):
    page = requests.get(url)
    page_soup = soup(page.content, 'html.parser')
    #print(page_soup)
    containers = page_soup.find_all(class_="MultiArticleComponenta ArticleHeadlinesAuto englishSite withoutImage")
    #print(containers)
    links = []
    links2 = []
    for ul in containers:
        links.extend(ul.findAll('a'))
    for link in links:
        links2.append(link.get('href'))
    #print(links2)
    #print(links2[0])
    return links2
    
    
    
def get_content_string(links):
    print(links[3])
    page = requests.get(links[3])
    page_soup = soup(page.content, 'html.parser')
    containers = page_soup.find_all(class_="layoutItem article-body-english")
    #print(containers)
    links = []
    links2 = []
 
    for ul in containers:
        links.extend(ul.findAll('span'))

    #print(links)
    text = page_soup.get_text()
    text = " ".join(text.split())
    print(text)
    
    for link in links:
        links2.append(link.get('data-text'))

    #print(links2)

 
    
    
links = get_content_links(my_url)
get_content_string(links)