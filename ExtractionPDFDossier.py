#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 14:09:12 2017

@author: AntoineP
"""
import requests
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
import io
import os
import re
import time


suffix='https://iopscience-iop-org.docadis.ups-tlse.fr'
contenu = open('data.json', 'r', encoding='utf8').read()
Json = json.loads(contenu)
  
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'MDP-WSSO-SESSION=b41e4f97b77b6d2c7aa74224913eb5ad; _ceg.s=om3n9g; _ceg.u=om3n9g; IOP_session_liveIDXWSSODOMAIN.iop.org=%2F%2F1488310191437%7C39cf8f54-225a-483d-a029-44b869926f15%7C20170228-cb0954e21ac6ac7a822d1a44ba7d9b55%7C%7C%7C%7C%7C%7C%7C%7C%7C0_26972%2Fa8c0ae88ee01b51908e40163b05982b2; cdnIDXWSSODOMAIN.optimizely.com=http%3a%2f%2fakamai%3adsd%40cdn.optimizely.com%2fjs%2f2290660256.js; __utma=23867810.382099440.1488309826.1488309826.1488309826.1; __utmb=23867810.0.10.1488309826; __utmc=23867810; __utmz=23867810.1488309826.1.1.utmcsr=cas.ups-tlse.fr|utmccn=(referral)|utmcmd=referral|utmcct=/cas/login',
    'Host':'iopscience-iop-org.docadis.ups-tlse.fr',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
    
#lien = 'https://iopscience-iop-org.docadis.ups-tlse.fr/article/10.1088/1674-1056/24/11/110309/pdf'
#r = requests.get(lien, headers=headers)
file_path= '//Users/AntoineP/Downloads/'
#directory = os.path.dirname(file_path)

try:
    os.makedirs('PDF')
except:
    print('PDF existe déjà')
    
for j in range(100,150):
    lien=Json[j]['lienPDF']
    search = requests.get(suffix + lien, headers=headers)
    while str(search)=='<Response [503]>':
        time.sleep(15)
        search = requests.get(suffix + lien, headers=headers)
        
    titre=Json[j]['titre']
    titre = re.sub(r'/',r'', titre)
    with open('PDF/['+str(j)+']'+titre + '.pdf', 'wb') as f:
        f.write(search.content)
    time.sleep(30)
#    memoire= io.BytesIO(search)
#    parser = PDFParser(memoire)
#    doc = PDFDocument()
#    parser.set_document(doc)
#    doc.set_parser(parser)
#    doc.initialize('')
#    rsrcmgr = PDFResourceManager()
#    laparams = LAParams()
#    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
#    interpreter = PDFPageInterpreter(rsrcmgr, device)
#    for page in doc.get_pages():
#        interpreter.process_page(page)
#        layout = device.get_result()
#        for lt_obj in layout:
#            if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
#                print(lt_obj.get_text())

    
#    with open('//Users/AntoineP/Downloads/PDFfcdsghj.pdf', 'wb') as f:
#        f.write(r.content)
#cookie = r.headers
#
#parser = PDFParser(r.content)
#doc = PDFDocument()
#parser.set_document(doc)

