#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:06:51 2022

@author: alex
"""
import random
import sqlite3
import itertools
from sqlite3 import Error


def create_database(text):
    data_base = create_connection(r"ynet_data.db")
    cur = data_base.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS articles
               (Sports text, Politics text, Finance text, Weather text)''')
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
    print(list_text)
    
    for catagory, word in itertools.product(sports, list_text):
        if catagory == word:
            print(word)
            text_catagory.append('sports')
            break
    for catagory, word in itertools.product(politics, list_text):
        if catagory == word:
            print(word)
            text_catagory.append('politics')
            break
    for catagory, word in itertools.product(finance, list_text):
        if catagory == word:
            print(word)
            print(text.find(catagory))
            text_catagory.append('finance')
            break   
    for catagory, word in itertools.product(weather, list_text):            
        if catagory == word:
            print(word)
            print(text.find(catagory))
            text_catagory.append('weather')
            break
    if text_catagory:
        random_catagory = random.choice(text_catagory) # if more than 2 categories
        print(random_catagory)
    
            
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
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