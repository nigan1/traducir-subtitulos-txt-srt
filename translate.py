#googletrans 3.1.0a0
from googletrans import Translator
import os


DIRECTORIO_BASE = os.path.dirname(__file__)

DIRECTORIO_ANALIZAR = os.path.join(DIRECTORIO_BASE, 'translate')

DIRECTORIO_ANALIZADO = os.listdir(DIRECTORIO_ANALIZAR)
#print(DIRECTORIO_ANALIZADO)

os.chdir(DIRECTORIO_ANALIZAR)

for document in DIRECTORIO_ANALIZADO:
    f=open(document,'r',encoding="utf-8")
    contents = f.read()
    file_translate = Translator()
    result = file_translate.translate(contents, dest='es')
    with open('ES-'+document, 'w',encoding="utf-8") as f:
        f.write(result.text)
    
print("traduccion completada")