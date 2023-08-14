# Criar formato csv necessário para o keras-retinanet - https://github.com/fizyr/keras-retinanet

from image_aq.utils.pascal_voc_io import PascalVocReader

with open('keras-retinanet.csv', 'w', newline='') as kerascsv:
    writer = csv.writer(kerascsv)
    for xml in glob.glob(IMG_PATH+'*stamp.xml'):
        # print(xml)
        voc_reader = PascalVocReader(xml)
        for shape in voc_reader.shapes:
            #print(shape)
            classe = shape[0]
            coords = shape[1]
            # x1, y1, x2, y2 - Ver pascal_voc_io.py linha 152 E
            # https://github.com/fizyr/keras-retinanet/README #AnnotationsFormat
            coords = (coords[0][0], coords[0][1], coords[2][0], coords[2][1])
            # print(coords)
            line = (xml[:-3]+'jpg', *coords, 'cc')
            # print(line)
            writer.writerow(line)
        
!echo 'cc,0' > classes.txt
