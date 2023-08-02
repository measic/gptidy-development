from image_aq.utils.pascal_voc_io import PascalVocWriter

def function_def(file):
    foldername, filename = os.path.split(file)
    img = imageio.imread(file)
    imgSize = img.shape
    print(foldername, filename, imgSize)
    voc_writer = PascalVocWriter(foldername, filename, imgSize)
    coords = find_conteiner(file)
    voc_writer.addBndBox(*coords, 'cc', '')
    voc_writer.save(file[:-4] + '.xml')
file = lista[0]
print(file)
function_def(file)
glob.glob(foldername + '/*')