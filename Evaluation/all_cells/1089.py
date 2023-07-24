import p5_util
if True:
    VGG16Seq = p5_util.object_load('./data/VGG16Seq_sgd.dump')
    VGG16Seq.summary()

import p5_util
import P7_DataBreed
if False :
    oP7_DataBreed = p5_util.object_load('./data/oP7_DataBreed.dump')
    oP7_DataBreed.show()
    oP7_DataBreed.breed_show()
