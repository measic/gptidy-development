# Copiar anotações já revisadas com LabelImg - anotar manualmente último contêiner trabalhado no LabelImg 
# para não copiar labels não revisados
from shutil import copyfile

IMG_PATH = '../image_aq/files/conteiner_to_check/'
cont = 0
for file in lista[100:1000]:
    cont +=1
    # print(file)
    basename = os.path.basename(file)
    # print(basename)
    copyfile(file, os.path.join(IMG_PATH, basename))
    copyfile(file[:-4]+'.xml', os.path.join(IMG_PATH, basename[:-4]+'.xml'))
    #if file.find('CMAU122') != -1:
    #    break
print(cont)