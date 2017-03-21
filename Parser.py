
from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LAParams, LTTextBox, LTTextLine , LTImage , LTFigure, LTCurve
import io
import os
import re
import time
import logging 
import numpy as np
from stemming.porter2 import stem
from Ranking import Ranking
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

for i in range(1,numPage):
    for elem in txtPage[i]:
        caption=dict()
        match = re.search("^Figure [0-9]+\.", elem) 
        if match:
            caption['numFigure']=re.sub(r'^Figure ([0-9])+\.(.|\n)*',r'\1', elem)
            caption['Figure'] = elem
            caption['Page'] = i
            caption['Ref'] = []
            ok.append(caption)
            

#Extraction des références directes aux figures


for i in range(1,numPage):
    for elem in txtPage[i]:
        ref=dict()
        match = re.search("(F|f)igure [0-9]+", elem) 
        if match and (elem not in [item['Figure'] for item in ok]):
            #Il peut y avoir plusieurs références dans le même paragraphe
            findAll = re.findall("[F|f]igure [0-9]+", elem) 
            refList=list()
            for fig in findAll: 
                num=re.sub(r'(.|\n)*([0-9])+',r'\2', fig)
                relatedFigure = [item for item in ok if item['numFigure'] == num]
                numIndex= ok.index(relatedFigure[0])
                ref['Ref'] = elem
                ref['Page'] = i
                ref['ValidatedByRanking']= "No"
                ref['FindBy'] = 'Direct reference'
                ok[numIndex]['Ref'].append(ref)
            
#Chercher d'autres références et vérifier si les références directes sont corréléés

a=Ranking()
tableau=[elem for page in txtPage for elem in txtPage[page]]
a.getVectorKeywordIndex(tableau)
a.matrixVector(tableau) 

for item in ok:
    score = a.search(item['Figure'])
    indexHighScore = [score.index(elem) for elem in score if (elem > 0.4)]
    for index in indexHighScore:
        #On vérifie si les références ne sont pas en fait les légendes 
        if (tableau[index] not in [elem['Figure'] for elem in ok]):
            #Dans le cas la référérence est une référence directe déjà trouvée
#            refDirecte = [j[i] for elem in item if elem == 'Ref' for j in item[elem] for i in j if i=='Ref']
#            if (tableau[index] in refDirecte):
                existing=False
                for reference in item['Ref']:
                    if (tableau[index] == reference['Ref']):
                        ok[ok.index(item)]['Ref'][item['Ref'].index(reference)]['ValidatedByRanking'] = "Yes"
                        existing =True
                if not existing:
                    ref=dict()
                    ref['Ref'] = tableau[index]
                    ref['Page'] = "?"
                    ref['ValidatedByRanking']= "Find by ranking"
                    ref['FindBy'] = 'Ranking reference'
                    ok[ok.index(item)]['Ref'].append(ref)
                    

                
                #ok[numIndex]['Ref'].append(ref)
#                print(relatedFigureIndex)
#                print(tableau[index])
#            

"""main:a=Parser(),
tableau=[elem for page in txtPage for elem in txtPage[page]],
a=Ranking()
a.getVectorKeywordIndex(tableau)
a.matrixVector(tableau)
a.search('Figure 9. (a) CT and (b)–(h) synthetic CT from seven different air masks generated by: (b) UTE images, (c) bias-corrected UTE images, (d) bias-corrected UTE images with a 1 mm expansion, (e) PETRA images, (f) bias-corrected PETRA images, (g) bias- corrected PETRA images with a 1mm expansion, and (h) bias-corrected PETRA images with a 2 mm expansion.')
Compte de chaque mot par paragraphe : a.documentVectors
a.search(legende)
[r.index(elem) for elem in r if (elem > 0.2)]
"""
#import RAKE
#Rake = RAKE.Rake('SmartStoplist.txt');
## You can use one of the stoplists included in the repository under stoplists/
#Rake.run('across patients, but low intensities were often observed in superior and/or posterior regions of \nthe head. Pre-scan normalization resulted in different bias fields than B1 normalization when \nevaluated using N4itk (figures 2(a)–(f)). Correcting these bias fields by using N4itk reduced \nintensity variations in the brain regions of the MR images (figure 2).\nPost-processing bias field correction improved the performance of UTE and PETRA \nimages for separation of air from bone. The bias-corrected UTE and PETRA images yielded \nareas under the ROC curves (AUCs) of 0.976 \xa0 ±\xa0 0.003 (Mean\xa0 ±\xa0 standard error) (n = 12) \nand 0.887 \xa0±\xa0 0.012 (n = 5), respectively, which were greater than those (0.944 \xa0±\xa0 0.012 and \n0.850 \xa0 ±\xa0 0.022) from the uncorrected images (figure 3 and table\xa0 1). The improvement in \nair masking when using N4itk to correct the bias field on the UTE images was significant  \n(p = 0.02), but not on the PETRA images (p = 0.1). Also, the AUC for air masking using the \nbias-corrected UTE images was significantly greater than the similarly-processed PETRA \n')