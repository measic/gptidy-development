filter_path = pcc.defaults._default_filter_dir_path
coco_root_path = pcc.defaults._default_coco_dir_path

reload(pccsims)
coco = pccsims.pyCoCo(pcc.utils.b(filter_path), pcc.utils.b(coco_root_path))