# load model
name_model = path + '/models_out/model_unet_64_flip_rot90_all_cl.h5'    
model_unet = load_model(name_model, custom_objects={'fn': ignore_background_class_accuracy(0)})