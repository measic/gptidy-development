from image_aq.utils.pascal_voc_io import PascalVocWriter

def gera_voc(file):
    foldername, filename = os.path.split(file)
    img = imageio.imread(file)
    imgSize = img.shape
    print(foldername, filename, imgSize)
    variable_def = PascalVocWriter(foldername, filename, imgSize)
    coords = find_conteiner(file)
    variable_def.addBndBox(*coords, 'cc', '')
    variable_def.save(file[:-4] + '.xml')
file = lista[0]
print(file)
gera_voc(file)
glob.glob(foldername + '/*')