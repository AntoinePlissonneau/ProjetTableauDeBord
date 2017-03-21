#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 15:59:18 2017

@author: AntoineP
"""
import numpy as np
from stemming.porter2 import stem
import re
from sklearn.feature_extraction.text import TfidfTransformer

class Ranking:
    vectorKeywordIndex = []
    documentVectors = []
    def __init__(self):
        self.stopwords= open('SmartStoplist.txt','r').read().split()
    
    #1/Tronquer les mots (stemming)
    def clean(self, string):
         string = string.replace(".","")
         string = string.replace("(","")
         string = string.replace(")","")
         string = re.sub(r"[0-9]","",string)
         string = string.replace("\s+"," ")
         string = string.lower()
         return string
    def tokenise(self, string):
         """ break string up into tokens and stem words """
         string = self.clean(string)
         words = string.split()
         return [stem(word) for word in words]
    #2/Stoplist
    
    def removeStopWords(self,list):
         """ Remove common words which have no search value """
         return [word for word in list if word not in self.stopwords ]
    """!!!!!!!!
    a=Parser()
    a.removeStopWords(b)
    """
    
    #3/Map keywords to vector
    """
    
    tableau=[elem for page in txtPage for elem in txtPage[page]]
    """
    
    def getVectorKeywordIndex(self, documentList):
            """ create the keyword associated to the position of the elements within the document vectors """
    
            #Mapped documents into a single word string
            vocabularyString = " ".join(documentList)
    
            vocabularyList = self.tokenise(vocabularyString)
            #Remove common words which have no search value
            vocabularyList = self.removeStopWords(vocabularyList)
            #Supprime les mots multiples
            uniqueVocabularyList = list(set(vocabularyList))
    
            vectorIndex={}
            offset=0
            #Associate a position with the keywords which maps to the dimension on the vector used to represent this word
            for word in uniqueVocabularyList:
                    vectorIndex[word]=offset
                    offset+=1
            self.vectorKeywordIndex =vectorIndex
            return vectorIndex  #(keyword:position)
    #4/tf-idf et creer les vecteurs
    #Va renvoyer un vecteur avec le score de chaque terme
    def makeVector(self, wordString):
            """ @pre: unique(vectorIndex) """
    
            #Initialise vector with 0's
            vector = [0] * len(self.vectorKeywordIndex)
            wordList = self.tokenise(wordString)
            wordList = self.removeStopWords(wordList)
            for word in wordList:
                    vector[self.vectorKeywordIndex[word]] += 1; #Use simple Term Count Model
            
            return vector
    """ y=a.makeVector(tableau[6],tableau)"""
    
                      
    def matrixVector(self, documents):
            """ Create the vector space for the passed document strings """
            matrix = [self.makeVector(document) for document in documents]
            transformer = TfidfTransformer(smooth_idf=True)
            tfidf = transformer.fit_transform(matrix)       
            self.documentVectors = tfidf.toarray().tolist()
            print("Matrice des vecteurs de chaque paragraphe du document crée")
        
    #5/Cosine
    def cosineVector(vector1, vector2):
            """ related documents j and q are in the concept space by comparing the vectors :cosine  = ( V1 * V2 ) / ||V1|| x ||V2|| """
            if (np.linalg.norm(vector1) != 0) and (np.linalg.norm(vector2) != 0):
                return float(np.dot(vector1,vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
            else:
                return 0
        
    #6/Search and score
    def search(self,searchList):
            """ search for documents that match based on a list of terms """
            transformer = TfidfTransformer(smooth_idf=True)
            queryVector = self.makeVector(searchList)
            tfidf = transformer.fit_transform(queryVector)
            queryVector = tfidf.toarray().tolist()
            ratings = [cosineVector(queryVector, documentVector) for documentVector in self.documentVectors]
            return ratings