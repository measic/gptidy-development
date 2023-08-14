import pandas as pd
import p5_util
import p6_util_plot
is_dumped=True
if is_dumped is True:
    filename = './data/dict_cls_score.dump'
    dict_cls_score = p5_util.object_load(filename)
else :
    pass

dict_cls_score['VGG16 Seq'] = score_vgg16_seq
dict_benchmark_result = dict_cls_score.copy()

df_result = pd.DataFrame.from_dict( dict_benchmark_result, orient='index')
df_result.reset_index(inplace=True)
df_result.rename(columns={'index':'Classifier',0:'Score'}, inplace=True)
df_result
nb_images = oP7_DataBreed._sampling_breed_count*oP7_DataBreed._sampling_image_per_breed_count
nb_images = oP7_DataBreed.df_pil_image_kpdesc.shape[0]
if oP7_DataBreed.is_kp_filtered :
    title = "Benchmark classifiers accuracy / GMM clustering / "+str(nb_images)+" filtered splitted images / "+str(oP7_DataBreed.sampling_breed_count)+" breeds"
else :
    title = "Benchmark classifiers accuracy / GMM clustering / "+str(nb_images)+" splitted images / "+str(oP7_DataBreed.sampling_breed_count)+" breeds"

p6_util_plot.ser_item_occurency_plot(df_result.Classifier, df_result.Score*100, item_count=None, title=title,\
                                    p_reverse=False,p_x_title='Classifiers', p_y_title='Accuracy')

#### Classifier API
p5_util.object_dump(dict_cls_score,filename)

dict_cls_score