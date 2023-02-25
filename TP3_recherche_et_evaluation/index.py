# -*- coding: utf-8 -*-
"""
Created on Thu Feb 16 09:50:12 2023

@author: esto5
"""

import os
import json
from nltk.tokenize import RegexpTokenizer
from nltk.stem.porter import *
import math
import numpy as np

#return the content of all the file of an folder
def loads(folder_path):
    retour=[[2],[]]
    for filename in os.listdir(folder_path):
        retour[0].append(filename)
        retour[1].append(Load(folder_path+filename))
    return retour

#return the content of a file
def Load(file_path):
    file_name, file_extension = os.path.splitext(file_path)
    with open(file_path,"r") as file:
        if file_extension == ".json":
            return json.load(file)
        else:
             return file.read()
            

def Main():
    #load our data
    index_invert = loads("../TP2_ constitution de vocabulaire et representation/Dico+tf_idf/")
    vocabulary = Load("../TP2_ constitution de vocabulaire et representation/vocabulaire.json") 
    normes = Load("../TP2_ constitution de vocabulaire et representation/normes.json") 
    
    #prepare the tokenizer qnd troncature
    tokenizer=RegexpTokenizer('[a-z]\w+')
    stemmer = PorterStemmer() #stemmer object for get the root of the word
    
    while True:
        request = input("What is your request ?").lower()   #get the request

        if request == "" or request == "q": #if empty we have end up
            break 
        
        dico={}
        words=tokenizer.tokenize(request) #get our words
        
        #get our tf
        for word in words:
            word = stemmer.stem(word)
            if word in dico:
                dico[word]=dico[word]+1
            else:
                dico[word]=1
        
        norme=0 #norme de la requete
        for word in dico:
            if word in vocabulary:
                norme = norme + (dico[word]*vocabulary[word])**2
        norme = math.sqrt(norme)
        
        #get tf_idf
        dico_invert={}
        for i in range(len(index_invert[1])):
            for word in index_invert[1][i]:
                if word in dico:
                    dico_invert[index_invert[0][i]]=index_invert[1][i][word]*norme/(normes[index_invert[0][i]]*norme)
        
        dico_invert = sorted(dico_invert.items(), key=lambda x: x[1], reverse=True)
        
        n=5
        if len(dico_invert)<n:
            n = len(dico_invert)
        
        #print the result for all the words
        for i in range(n):
            print(dico_invert[i])

Main()