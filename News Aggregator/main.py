#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 11:22:13 2022

@author: alex
"""


import database
import time

my_url = "https://www.ynetnews.com/category/3089"

 

def main():
    #links = news_extract.get_content_links(my_url)
    #text = news_extract.get_content_string(links)
    #print(text[2])
    #print(type(text))

    #database.create_database(my_url)
    user = input("What is your name?\n")
    email_address = input("What is your email address? \n")
    news_category_list = []
    print("For what category you would like to subscribe? \n")
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
    preference_dict = {}
    while 1:
        if preference.lower() == "asap":
            preference_dict [preference] = "asap"
            break
        elif preference.lower() == "daily":
            time_list = []
            print("Please enter the time to receive: \n")
            while 1:
                user_input = input()                
                if user_input.lower() == "end":
                    break                
                else :
                    print("Add another time or enter 'end' \n")
                    time_list.append(user_input)
                    # if preference not in preference_dict:
                    #     preference_dict[preference] = list()
                    # preference_dict[preference].extend(int(user_input))
            time_list = list(dict.fromkeys(time_list))# delete duplicates
            preference_dict[preference] = time_list
            break
        elif preference.lower() == "weekly":
            
            print("Please enter what day you want to receive: \n")
            while 1:
                user_input = input()              
                if user_input.lower() == "end":
                    break                
                else :
                    user_input2 = input("Please enter what time: \n")
                    print("Add another day or enter 'end' \n")
                    preference_dict[user_input] = user_input2
            break
        else :
            print("please enter the right preference: ASAP/Daily/Weekly\n")    
            time.sleep(1)
    print(preference_dict)
    
    
    database.add_user(user, email_address, news_category_list, preference_dict)

if __name__ == "__main__":
    main()