#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 11:56:08 2023

@author: venon
"""

import os
from nltk.tokenize import RegexpTokenizer
#collection_tokens

def Main(link):
    for filename in os.listdir(link):
        file=open(link+filename,"r")
        content=file.read().lower()
        tokenizer=RegexpTokenizer('[a-z]\w+')
        words=tokenizer.tokenize(content)
        file.close()
        file=open("collection_tokens/"+filename+".tok","w")
        file.truncate(0)
        for word in words:
            file.write(word+"\n")
        file.close()
        
    
    
Main("collection/")