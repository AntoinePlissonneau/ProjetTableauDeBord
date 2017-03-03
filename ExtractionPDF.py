import urllib.request
import requests
from bs4 import BeautifulSoup
import re
import json

def pbEncodage(text):
    return re.sub(r'\xa0',r' ', text);  

#Contient toutes les métadonnées des docs
corpus=list()
cpt=0
for i in range(100):
    
    url="http://iopscience.iop.org/nsearch?terms=search&nextPage=0&previousPage=-1&pageLength=10&currentPage="+str(i)+"&searchType=fullText&page=&navsubmit=GoNext&articleid_1742-6596%2F776%2F1%2F012113=1742-6596%2F776%2F1%2F012113&articleid_1674-1056%2F24%2F11%2F110309=1674-1056%2F24%2F11%2F110309&articleid_0295-5075%2F82%2F2%2F20001=0295-5075%2F82%2F2%2F20001&articleid_1478-3975%2F12%2F4%2F046012=1478-3975%2F12%2F4%2F046012&articleid_0004-637X%2F777%2F1%2F70=0004-637X%2F777%2F1%2F70&articleid_0004-637X%2F692%2F1%2F942=0004-637X%2F692%2F1%2F942&articleid_1755-1315%2F31%2F1%2F012015=1755-1315%2F31%2F1%2F012015&articleid_0004-637X%2F761%2F2%2F88=0004-637X%2F761%2F2%2F88&articleid_1538-3873%2F123%2F909%2F1324=1538-3873%2F123%2F909%2F1324&articleid_1742-6596%2F623%2F1%2F012013=1742-6596%2F623%2F1%2F012013&navsubmit=GoNext"
    r = requests.get(url)
    soup = BeautifulSoup(r.text,'html.parser')
    
    result = soup.find_all('li',attrs={"class":u"articleSearchResultItem"})
    
    for item in result:
        doc=dict()
        doc['Id']=cpt
        #Auteur
        authors=item.find('p',attrs={"class":u"authorList"})
        if authors is not None:
            authors=pbEncodage(authors.text)
        else:
            authors=''
        doc['Autheur']= authors    
           
        #Année (à re)
        annee = pbEncodage(item.find_all('p')[1].text)
        annee = re.sub(r'(\d{4}).*',r'\1', annee)
        doc['Annee']= annee
        #Résumé
        successfull=False
        try:
            resume = item.find_all('p')[2]
            successfull=True
        except:
            print('raté')
        if (resume is not None) and (successfull):
            resume=pbEncodage(resume.text)
        else:
            resume=''
        doc['Resume']= resume
        #titre
        titre = pbEncodage(item.find('a').text)
        doc['Titre']= titre
        #type
        typeDoc = pbEncodage(item.find('span').text)
        doc['Type']= typeDoc
        #Lien vers pdf (vérifier si lien actif)
        
        lienPDF= item.find('a',attrs={"class":u"icon pdf"})
        if lienPDF is not None:
            lienPDF=lienPDF.get('href')
        else:
            lienPDF=''
        doc['LienPDF']= lienPDF
        
        #doi
        doi = item.find('span' , {'class':"doi"}).text
        doi = re.sub(r'doi:(.*)',r'\1', doi)
        #print(doi)
        doc['doi'] = doi
        
        corpus.append(doc)
        cpt=cpt+1
        #print(doc)
    
with open('data.json', 'w', encoding='utf8') as json_file:
    json.dump(corpus, json_file, ensure_ascii=False)    
    
    
    
    
    
    
    
    
    





































