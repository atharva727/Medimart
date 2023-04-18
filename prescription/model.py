from doctr.models import ocr_predictor
from doctr.io import DocumentFile
import textdistance

def getText(imagePath):
    model = ocr_predictor(pretrained=True)
    
    doc = DocumentFile.from_images(imagePath)
    result = model(doc)
    text=result.render()    
    
    return text



# W = set(w)
def autoCorrect(inputWord,WORDS):

    inputWord = inputWord.lower()
    if inputWord in WORDS:
        return (inputWord,1)
    
    maxSim = 0
    sim = 0
    d = {}
    for v in WORDS:
        sim = 1-(textdistance.Jaccard(qval=1).distance(v,inputWord))
        maxSim = max(maxSim,sim)
        d[sim] = v
    
    # print(inputWord,d[maxSim],sim,sep="   ")
    return (d[maxSim],sim)
