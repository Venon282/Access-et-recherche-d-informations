#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13 12:35:50 2023

@author: venon
"""

import os

def Main(link,n):
    dico={}
    for filename in os.listdir(link):
        with open(link+filename,"r") as file:
            for line in file:
                if line not in dico:
                    dico[line]=1
                else: dico[line]+=1
    dico = dict(sorted(dico.items(), key=lambda item: item[1], reverse=True))
    with open("result.txt","w") as file:
        counter=0
        for word in dico:
            if counter==n:
                break
            file.write(word.strip() +' ' + str(dico[word])+"\n")
            counter+=1
        file.write("\nNumber of words : " + str(len(dico)) +"\n")
        
    
    
Main("collection_tokens/",10)