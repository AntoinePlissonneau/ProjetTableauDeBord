#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 15:11:22 2017

@author: AntoineP
"""

import urllib.request
import requests
from bs4 import BeautifulSoup
import re
import json

def pbEncodage(text):
    return re.sub(r'\xa0',r' ', text);  

#Contient toutes les métadonnées des docs
corpus=list()
for i in range(20):
    
    url="http://iopscience.iop.org/nsearch?terms=search&nextPage=0&previousPage=-1&pageLength=10&currentPage="+str(i)+"&searchType=fullText&page=&navsubmit=GoNext&articleid_1742-6596%2F776%2F1%2F012113=1742-6596%2F776%2F1%2F012113&articleid_1674-1056%2F24%2F11%2F110309=1674-1056%2F24%2F11%2F110309&articleid_0295-5075%2F82%2F2%2F20001=0295-5075%2F82%2F2%2F20001&articleid_1478-3975%2F12%2F4%2F046012=1478-3975%2F12%2F4%2F046012&articleid_0004-637X%2F777%2F1%2F70=0004-637X%2F777%2F1%2F70&articleid_0004-637X%2F692%2F1%2F942=0004-637X%2F692%2F1%2F942&articleid_1755-1315%2F31%2F1%2F012015=1755-1315%2F31%2F1%2F012015&articleid_0004-637X%2F761%2F2%2F88=0004-637X%2F761%2F2%2F88&articleid_1538-3873%2F123%2F909%2F1324=1538-3873%2F123%2F909%2F1324&articleid_1742-6596%2F623%2F1%2F012013=1742-6596%2F623%2F1%2F012013&navsubmit=GoNext"
#    headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#'Accept-Encoding':'gzip, deflate, sdch, br',
#'Accept-Language':'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4',
#'Cache-Control':'max-age=0',
#'Connection':'keep-alive',
#'Cookie':'MDP-WSSO-SESSION=5f1e2c11a7b0fab883c387f1a97c9a47; IOP_session_liveIDXWSSODOMAIN.iop.org=%2F%2F1487694402155%7Cea4916e3-8670-4759-a4d1-17eaf8ad4a5c%7C20170221-33906b7e9933d55d859abd056876a1ac%7C%7C%7C%7C%7C%7C%7C%7C%7C0_26972%2Ff5abed1be9348c4b22528af9f4355f85; __utma=23867810.241777784.1487694405.1487694405.1487694405.1; __utmb=23867810.1.10.1487694405; __utmc=23867810; __utmz=23867810.1487694405.1.1.utmcsr=cas.ups-tlse.fr|utmccn=(referral)|utmcmd=referral|utmcct=/cas/login; _ceg.s=olqgck; _ceg.u=olqgck',
#'Host':'iopscience-iop-org.docadis.ups-tlse.fr',
#'Upgrade-Insecure-Requests':'1',
#'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
    r = requests.get(url)
#   r = urllib.request.urlopen(url,headers=headers)
    soup = BeautifulSoup(r.text,'html.parser')
    
    result = soup.find_all('li',attrs={"class":u"articleSearchResultItem"})
    
    for item in result:
        doc=dict()
        
        #Auteur
        authors=item.find('p',attrs={"class":u"authorList"})
        if authors is not None:
            authors=pbEncodage(authors.text)
        else:
            authors=''
        doc['authors']= authors    
           
        #Année (à re)
        annee = pbEncodage(item.find_all('p')[1].text)
        annee = re.sub(r'(\d{4}).*',r'\1', annee)
        doc['annee']= annee
        #Résumé
        successfull=False
        try:
            resume = item.find_all('p')[2]
            successfull=True
        except:
            print('fuck')
        if (resume is not None) and (successfull):
            resume=pbEncodage(resume.text)
        else:
            resume=''
        doc['resume']= resume
        #titre
        titre = pbEncodage(item.find('a').text)
        doc['titre']= titre
        #type
        typeDoc = pbEncodage(item.find('span').text)
        doc['type']= typeDoc
        #Lien vers pdf (vérifier si lien actif)
        
        lienPDF= item.find('a',attrs={"class":u"icon pdf"})
        if lienPDF is not None:
            lienPDF=lienPDF.get('href')
        else:
            lienPDF=''
        doc['lienPDF']= lienPDF
        
        #doi
        doi = item.find('span' , {'class':"doi"}).text
        doi = re.sub(r'doi:(.*)',r'\1', doi)
        print(doi)
        doc['doi'] = doi
        
        corpus.append(doc)
        print(doc)
    
with open('data.json', 'w', encoding='utf8') as json_file:
    json.dump(corpus, json_file, ensure_ascii=False)    
    
    
    
    
    
    
    
    
    





































