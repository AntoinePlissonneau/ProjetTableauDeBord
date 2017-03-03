import requests
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine
import io
import os
import re
import time


dossierPDF = 

lien="http://iopscience.iop.org/article/10.1209/0295-5075/112/42001/pdf"
print(lien)
search = urllib.request.urlopen(lien).read()
memoire= io.BytesIO(search)
parser = PDFParser(memoire)
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

        if isinstance(lt_obj, LTImage) or isinstance(lt_obj,LTFigure) or isinstance(lt_obj,LTCurve):
            print(lt_obj)
            save_image(lt_obj)
