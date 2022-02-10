#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:22:13 2022

@author: alex
"""


import database
import time
import sqlite3
from sqlite3 import Error
import sql
import pandas as pd
import smtplib
import send_links
import yagmail
import datetime as dt

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

my_url = "https://www.ynetnews.com/category/3089"

 

def main():
    
    #user creation and data/preferences
    user = input("What is your name?\n")
    email_address = input("What is your email address? \n")
    news_category_list = []
    print("For what category you would like to subscribe? \n")
    user_id = 1
    while 1:       
        news_category = input()
        if news_category.lower() == "sports":
            news_category_list.append(news_category)
        elif news_category.lower() == "politics":
            news_category_list.append(news_category)
        elif news_category.lower() == "finance":
            news_category_list.append(news_category)
        elif news_category.lower() == "weather":
            news_category_list.append(news_category)
        elif news_category.lower() == "end":
            break
        else :
            print("please enter the right category\n")
            time.sleep(1)
        print("Enter another category if you want or 'end' to continue to the next step\n")            
    news_category_list = list(dict.fromkeys(news_category_list))# delete duplicates
    print("What is your subscription preferences? ASAP/Daily/Weekly\n")
    preference = input()
    preference_list = []
    while 1:
        if preference.lower() == "asap":
            preference_list.append(preference)
            break
        elif preference.lower() == "daily":
            preference_list.append(preference)
            time_list = []
            print("Please enter the time to receive: \n")
            while 1:
                user_input = input()                
                if user_input.lower() == "end":
                    break                
                else :
                    print("Add another time or enter 'end' \n")
                    time_list.append(user_input)
            preference_list = list(dict.fromkeys(time_list))# delete duplicates
            break
        elif preference.lower() == "weekly":
            preference_list.append(preference)
            print("Please enter what day you want to receive: \n")
            while 1:
                user_input = input()              
                if user_input.lower() == "end":
                    break                
                else :
                    user_input2 = input("Please enter what time: \n")
                    print("Add another day or enter 'end' \n")
                    preference_list.append(user_input)
                    preference_list.append(user_input2)
            break
        else :
            print("please enter the right preference: ASAP/Daily/Weekly\n")    
            time.sleep(1)
    database.add_user(user_id ,user, email_address, news_category_list, preference_list)
    ++user_id
    database.create_database(my_url)    
    data_base = create_connection(r"ynet_data.db")
    cur = data_base.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    list_tables = cur.fetchall()
    list_tables = [r[0] for r in list_tables]
    list_tables.remove('articles')
    user = 'user_name'
    
    user_sql = sql.ReadSQL(r"ynet_data.db")
  
    
    for userin_list in list_tables:
    
        df = user_sql.query_columns_to_dataframe(userin_list,['user_name'])
        user = df.iloc[0][0]
        df = user_sql.query_columns_to_dataframe(userin_list,['email'])
        email = df.iloc[0][0]
        df = user_sql.query_columns_to_dataframe(userin_list,['categories'])
        categories_list = df["categories"].tolist()
        df = user_sql.query_columns_to_dataframe(userin_list,['preferences'])
        preferences_list = df["preferences"].tolist()
        categories_list = list(filter(None, categories_list))
        preferences_list = list(filter(None, preferences_list))
        sports = []
        politics = []
        finance = []
        weather = []
        
        for temp_list in categories_list:
            if temp_list == "sports":
                sports = send_links.send_links.sendBack_link(temp_list)
                sports = list(filter(None, sports))
            elif temp_list == "politics":
                politics = send_links.send_links.sendBack_link(temp_list)
                politics = list(filter(None, politics))
            elif temp_list == "finance":
                finance = send_links.send_links.sendBack_link(temp_list)
                finance = list(filter(None, finance))
            elif temp_list == "weather":
                weather = send_links.send_links.sendBack_link(temp_list)
                weather = list(filter(None, weather))
                
        if preferences_list[0] == "asap":
            send_email(sports, politics, finance, weather, email)            
        elif preferences_list[0] == "daily":
            preferences_list.remove("daily")
            for hours in preferences_list:
                first_email_time = dt.datetime(2022,2,10,1 * hours,0,0) # set your sending time in UTC
                interval = dt.timedelta(minutes=1) # set the interval for sending the email      
                send_time = first_email_time               
                send_email_at(send_time,sports, politics, finance, weather, email)
                send_time = send_time + interval   
        elif preferences_list[0] == "weekly1":
            preferences_list.remove("weekly")
            for hours in preferences_list:
                first_email_time = dt.datetime(2022,2,10,1 * hours,0,0) # set your sending time in UTC
                interval = dt.timedelta(minutes=1) # set the interval for sending the email      
                send_time = first_email_time               
                send_email_at(send_time,sports, politics, finance, weather, email)
                send_time = send_time + interval
    
    
    
    
def send_email(sports, politics, finance, weather, email):
    yag = yagmail.SMTP('alexcar18.bgu@gmail.com', 'car312795')
    
    yag.send(email, "This is your prefered news:)", sports+politics+finance+weather)
 
    
def send_email_at(send_time,sports, politics, finance, weather, email):
   time.sleep(send_time.timestamp() - time.time())
   send_email(sports, politics, finance, weather, email)
   print('email sent')
   
   
   
    # article = "articles"
    # ynet_sql = sql.ReadSQL(r"ynet_data.db")
    # df = ynet_sql.query_columns_to_dataframe(article,['politics'])
    # preferences_list = df["politics"].tolist()
    # print(preferences_list)
    
    
    
    #send by refernce
    
    
    
    
    # import yagmail
    # yag = yagmail.SMTP('alexcar18.bgu@gmail.com', 'car312795')
    
    # yag.send('alexcar18.bgu@gmail.com', "SUBJECT", "TEXT")
    
  
    
    
    
    #links = news_extract.get_content_links(my_url)
    #text = news_extract.get_content_string(links)
    #print(text[2])
    #print(type(text))

    
   
    
    
    
    
    #database.add_user(user, email_address, news_category_list, preference_dict)

if __name__ == "__main__":
    main()