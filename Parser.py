import requests
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine , LTImage , LTFigure, LTCurve
import io
import os
import re
import time
import logging 
ListePDF = os.listdir("PDF/")
for filename in ListePDF[:1] :
    print(filename)
fn = open("PDF/"+filename, 'rb')
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
for page in doc.get_pages():
    interpreter.process_page(page)
    layout = device.get_result()
    for lt_obj in layout:
        if isinstance(lt_obj, LTTextBox) or isinstance(lt_obj, LTTextLine):
            print(lt_obj.get_text())

        if isinstance(lt_obj, LTImage) or isinstance(lt_obj,LTFigure) :
            print(lt_obj)

    
