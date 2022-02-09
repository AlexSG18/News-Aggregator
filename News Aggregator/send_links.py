#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 18:41:02 2022

@author: alex
"""
import sql


class send_links():    
    
    def sendBack_link(categories_list):
        article = "articles"
        ynet_sql = sql.ReadSQL(r"ynet_data.db")
        df = ynet_sql.query_columns_to_dataframe(article,[categories_list])
        preferences_list = df[categories_list].tolist()
        
        
        return preferences_list