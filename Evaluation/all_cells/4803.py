# Fully train the SRGAN with VGG loss and Discriminator loss
srgan_network.train_full_model(coco_path, num_images=80000, epochs=5, batch_size=16)