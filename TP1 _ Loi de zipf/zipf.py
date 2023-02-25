#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 12:35:50 2023

@author: venon
"""

import os

def Main(link,n):
    dico={}
    #file flux
    for filename in os.listdir(link):
        with open(link+filename,"r") as file:
            #for each words
            for line in file:
                #if first time 1 occurance else 1 more
                if line not in dico:
                    dico[line]=1
                else: dico[line]+=1
    #decreasing sort
    dico = dict(sorted(dico.items(), key=lambda item: item[1], reverse=True))
    
    #Save the result
    with open("result.txt","w") as file:
        counter=0
        #for all our words
        for word in dico:
            #if n terme it's the end
            if counter==n:
                break
            #write the word
            file.write(word.strip() +' ' + str(dico[word])+"\n")
            counter+=1
        #write the number of words
        file.write("\nNumber of words : " + str(len(dico)) +"\n")
        
    
    
Main("collection_tokens/",10)