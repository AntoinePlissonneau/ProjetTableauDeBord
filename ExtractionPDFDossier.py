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
    'Cookie':'_ceg.s=om3n9g; _ceg.u=om3n9g; cdnIDXWSSODOMAIN.optimizely.com=http%3a%2f%2fakamai%3adsd%40cdn.optimizely.com%2fjs%2f2290660256.js; __utma=23867810.382099440.1488309826.1488313069.1488412463.3; __utmc=23867810; __utmz=23867810.1488309826.1.1.utmcsr=cas.ups-tlse.fr|utmccn=(referral)|utmcmd=referral|utmcct=/cas/login; MDP-WSSO-SESSION=6334603b9de452e5f3c871cf9ca541aa; IOP_session_liveIDXWSSODOMAIN.iop.org=%2F%2F1488465113594%7C11712cbd-4335-400d-94cd-d3ea4df3dda5%7C20170302-bd75206f42e125ed3d11d3fffa8f0acd%7C%7C%7C%7C%7C%7C%7C%7C%7C0_26972%2F51e84ccfc28786c698f9f39e65c4642d',
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
    
for j in range(0,1000):
    lien=Json[j]['LienPDF']
    search = requests.get(suffix + lien, headers=headers)
    while str(search)=='<Response [503]>':
        print('banned')
        time.sleep(15)
        search = requests.get(suffix + lien, headers=headers)
        
    titre=Json[j]['Titre']
    titre = re.sub(r'/',r'', titre)
    with open('PDF/['+str(Json[j]['Id'])+']'+titre + '.pdf', 'wb') as f:
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

