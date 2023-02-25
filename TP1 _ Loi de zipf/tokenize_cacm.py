#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 11:56:08 2023

@author: venon
"""

import os
from nltk.tokenize import RegexpTokenizer

#recovers the tokens
def GetTokens(link):
    #File flow
    for filename in os.listdir(link):
        
        file=open(link+filename,"r")
        content=file.read().lower() #get the content + in lower case
        tokenizer=RegexpTokenizer('[a-z]\w+') #regex
        words=tokenizer.tokenize(content)
        file.close()
        
        file=open("collection_tokens/"+filename+".tok","w")
        file.truncate(0)
        #Write all our words
        for word in words:
            file.write(word+"\n")
        file.close()
        
    
    
GetTokens("collection/")