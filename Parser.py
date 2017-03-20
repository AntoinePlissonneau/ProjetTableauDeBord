
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine , LTImage , LTFigure, LTCurve
import io
import os
import re
import time
import logging 
#ListePDF = os.listdir("PDF/")
#for filename in ListePDF :
#    print(filename)

fn = open("PDF/[119]Quantitative characterizations of ultrashort echo .pdf", 'rb')
logging.propagate = False
logging.getLogger().setLevel(logging.ERROR)
parser = PDFParser(fn)
doc = PDFDocument()
parser.set_document(doc)
doc.set_parser(parser)
doc.initialize('')
rsrcmgr = PDFResourceManager()
laparams = LAParams()
device = PDFPageAggregator(rsrcmgr, laparams=laparams)
interpreter = PDFPageInterpreter(rsrcmgr, device)
txt=[]
txtPage=dict()
numPage=0

#Extraction du text pour chaque page
for page in doc.get_pages():
    numPage+=1
    interpreter.process_page(page)
    layout = device.get_result()
    for lt_obj in layout:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            txt.append(lt_obj.get_text())

#        if isinstance(lt_obj, LTImage) or isinstance(lt_obj,LTFigure) :
#            print(lt_obj)
    txtPage[numPage] = txt
    txt=[]

#Extraction des légendes des figures pour chaque page
ok=list()
caption=dict()
for i in range(1,numPage):
    for elem in txtPage[i]:
        match = re.search("^Figure [0-9]+\.", elem) 
        if match:
            caption['numFigure']=re.sub(r'^Figure ([0-9])+\..*',r'\1', elem)
            caption['Figure'] = elem
            caption['Page'] = i
            print(caption)
            ok.append(caption)
            print("\n")
            print(ok)

#Extraction des références directes aux figures



#Im = Image, Fm= font?
    
