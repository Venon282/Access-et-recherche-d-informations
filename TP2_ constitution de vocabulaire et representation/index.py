#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 27 11:31:32 2023

@author: venon
"""

import os
from nltk.stem.porter import *
import json
import math

#get the document with their vocabulary
def AntiDico(tok_folder,commons_words_file,destination):
    stemmer = PorterStemmer() #stemmer object for get the root of the word
    #get our anti dictionnary
    with open(commons_words_file,"r") as file:
        content=file.read().split('\n')
    #put this array in dico
    dico={content[i]: 1 for i in range(0, len(content), 1)}
    
    #for all our files
    for filename in os.listdir(tok_folder):
        #we get its content
        with open(tok_folder+filename,"r") as file:
            content=file.read().lower()
        #rewrite it without the wrong words
        with open(destination+filename,'w') as file:
            for line in content.split('\n'):
                if line not in dico:
                    file.write(stemmer.stem(line)+'\n')

#get the vvocabulary of all our files
def Vocabulary(source,destination):
    dico_final={} #nb of document where is the word
    #create dictionary for document
    for filename in os.listdir(source):
        dico={}
        with open(source+filename,'r') as file:
            for line in file.read().split('\n'):
                if line not in dico:
                    dico[line]=1
        
        #concatenate the dico
        for cle in dico.keys():
            if cle not in dico_final:
                dico_final[cle]=1
            else: 
                dico_final[cle]=dico_final[cle]+dico[cle]
    
    #calcul de l'idf_i
    dico_final={cle:math.log(len(os.listdir(source))/dico_final[cle]) for cle in dico_final.keys()}
    
    #infill vocabulary with our data
    with open(destination+'vocabulaire.json','w') as file: 
        json.dump(dico_final,file)
        

def DicoWithOccurence(source_folder,destination):
    for filename in os.listdir(source_folder): #file browsing
        dico={}
        with open(source_folder+filename,'r') as file: #☺open the current file
            for line in file.read().strip().split('\n'):        #read it
                if line in dico :
                    dico[line]=dico[line]+1             #add the number of occurence
                else:
                    dico[line]=1
        
        with open(destination+filename.split('.')[0]+'.json','w') as file:
            json.dump(dico,file)
        
def Ponderation(source_file,source_voc,destination):
    for filename in os.listdir(source_file):
        dico={}
        with open(source_file+filename,'r') as file: 
            dico_j = json.load(file)
        with open(source_voc+'vocabulaire.json','r') as file:
            voc_j = json.load(file)
        for word in dico_j:
            dico[word]=dico_j[word]*voc_j[word]
        with open(destination+filename,'w') as file:
            json.dump(dico,file)
     

def Main():
    #AntiDico("../TP1 : Loi de zipf/collection_tokens/","common_words",'AntiDico apply/')
    #Vocabulary('AntiDico apply/','')
    DicoWithOccurence('AntiDico apply/','Dico+tf/')
    Ponderation('Dico+tf/','','Dico+tf_idf/')
    

Main()