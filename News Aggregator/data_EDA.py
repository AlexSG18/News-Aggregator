#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  9 20:37:25 2022

@author: alex
"""
from collections import Counter
import re
from nltk.corpus import stopwords
from string import digits


import collections
import pandas as pd
import matplotlib.pyplot as plt


from gensim.parsing.preprocessing import remove_stopwords


def collect_data(text):
    #print(text_catagory)
    # words = re.findall('\w+',text)
    # print(Counter(words).most_common(5))
    filtered_sentence = remove_stopwords(text)
    remove_digits = str.maketrans('', '', digits)
    filtered_sentence = filtered_sentence.translate(remove_digits)
   #print(filtered_sentence)
    words = re.findall('\w+',filtered_sentence)
    #print(Counter(words).most_common(7))
    nlp_list = Counter(words).most_common(7)
    df = pd.DataFrame(nlp_list, columns=['words', 'frequency'])


    df.plot(kind='bar', x='words')
    #plt.savefig('most_frq.png', dpi=500)
        
    

