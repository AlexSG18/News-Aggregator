#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:22:13 2022

@author: alex
"""


#import news_extract
import database

my_url = "https://www.ynetnews.com/category/3089"





    
    



def main():
    #links = news_extract.get_content_links(my_url)
    #text = news_extract.get_content_string(links)
    #print(text[2])
    #print(type(text))

    database.create_database(my_url)

if __name__ == "__main__":
    main()