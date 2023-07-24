# Path to MS COCO dataset
coco_path = r"tests/coco"


#Base Network manager for the SRGAN model

#Width / Height = 32 to reduce the memory requirement for the discriminator.

#Batch size = 1 is slower, but uses the least amount of gpu memory, and also acts as
#Instance Normalization (batch norm with 1 input image) which speeds up training slightly.

srgan_network = SRGANNetwork(img_width=32, img_height=32, batch_size=1)
srgan_network.build_srgan_model()
srgan_network.srgan_model_.summary()