#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:06:51 2022

@author: alex
"""
import random
import sqlite3
import news_extract
from sqlite3 import Error
from itertools import product



def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_database(my_url):
    
    data_base = create_connection(r"ynet_data.db")
    cur = data_base.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS articles
               (sports text, politics text, finance text, weather text)''')
    data_base.commit()
    links = news_extract.get_content_links(my_url)# get all links
    for link in links:
        text = news_extract.get_content_string(link)
        text_catagory = find_in_text(text)
        if text_catagory is not None:
            if text_catagory == 'sports':            
                cur.execute("INSERT INTO articles (politics) VALUES(?)",(link, ))
                data_base.commit()
            elif text_catagory == 'politics':            
                cur.execute("INSERT INTO articles (politics) VALUES(?)",(link, ))
                data_base.commit()
            elif text_catagory == 'finance':            
                cur.execute("INSERT INTO articles (politics) VALUES(?)",(link, ))
                data_base.commit()
            elif text_catagory == 'weather':            
                cur.execute("INSERT INTO articles (politics) VALUES(?)",(link, ))
                data_base.commit()
        
        
    

    
# Method Purpose: This method finds the chosen categories from each article
def find_in_text(text):
    sports = ['football', 'basketball', 'ski', 'sport', 'olympics', 'athletics', 'tournament']
    politics = ['president', 'prime', 'minister', 'law', 'U.N', 'NATO', 'government', 'democrats',
                'republicans', 'minister', 'vote', 'politician', 'political', 'party']   
    finance = ['dollar', 'stocks', 'shekel', 'bitcoin', 'company', 'sp500', 'nasdaq']    
    weather = ['rain', 'snow', 'sunny', 'earthquake', 'clouds', 'storm', 'flood']
    
    text_catagory = []
    list_text = text.lower().split(" ")    
    for catagory, word in product(sports, list_text):
        if catagory == word:
            text_catagory.append('sports')
            break
    for catagory, word in product(politics, list_text):
        if catagory == word:
            text_catagory.append('politics')
            break
    for catagory, word in product(finance, list_text):
        if catagory == word:
            text_catagory.append('finance')
            break   
    for catagory, word in product(weather, list_text):            
        if catagory == word:
            text_catagory.append('weather')
            break
    #print(text_catagory)
    if text_catagory:
        random_catagory = random.choice(text_catagory) # if more than 2 categories
        #print("1" + random_catagory)
        return random_catagory
    
    return None
    
    
    
   
    
