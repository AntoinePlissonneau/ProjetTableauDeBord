#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 22:12:04 2017

@author: AntoineP
"""

from pymongo import MongoClient
import json
client = MongoClient()
client = MongoClient('localhost', 27017)
db = client.tableau_de_bord
contenu = open("data3.json","r", encoding='utf8').read()
Json = json.loads(contenu)
posts = db.posts
for elem in Json:
    post_id = posts.insert_one(elem).inserted_id
post_id