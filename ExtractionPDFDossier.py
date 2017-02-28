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
contenu = open('//Users/AntoineP/Downloads/data.json', 'r', encoding='utf8').read()
Json = json.loads(contenu)
  
headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding':'gzip, deflate, sdch, br',
    'Accept-Language':'fr-FR,fr;q=0.8,en-US;q=0.6,en;q=0.4',
    'Cache-Control':'max-age=0',
    'Connection':'keep-alive',
    'Cookie':'MDP-WSSO-SESSION=77dbc2056652a4c79911152fd2dfc179; IOP_session_liveIDXWSSODOMAIN.iop.org=%2F%2F1488297473442%7C224eb2d4-a138-475e-a805-6dc9eff33c42%7C20170228-13fe63d869a1f9746a21648a187ef5d6%7C%7C%7C%7C%7C%7C%7C%7C%7C0_26972%2F849d70c48f9dc085ed7229633df7ebc4',
    'Host':'iopscience-iop-org.docadis.ups-tlse.fr',
    'Upgrade-Insecure-Requests':'1',
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.95 Safari/537.36'}
    
#lien = 'https://iopscience-iop-org.docadis.ups-tlse.fr/article/10.1088/1674-1056/24/11/110309/pdf'
#r = requests.get(lien, headers=headers)
file_path= '//Users/AntoineP/Downloads/'
#directory = os.path.dirname(file_path)

try:
    os.makedirs('//Users/AntoineP/Downloads/caca')
except:
    print('caca')
    
for j in Json:
    lien=j['lienPDF']
    
    search = requests.get(suffix + lien, headers=headers)
    titre=j['titre']
    titre = re.sub(r'/',r'', titre)
    with open('//Users/AntoineP/Downloads/caca/'+ titre + '.pdf', 'wb') as f:
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

