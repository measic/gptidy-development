import p5_util
is_score_dumped=True
if is_score_dumped is True :
    filename = './data/dict_cls_score.dump'
    dict_cls_score = p5_util.object_load(filename)
else:
    dict_cls_score = dict()
dict_classifier = dict()

dict_cls_score