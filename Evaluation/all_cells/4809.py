coco_path = "tests/coco"

img_width = img_height = 64

sr_resnet_test = SRResNetTest(img_width=img_width, img_height=img_height, batch_size=1)
sr_resnet_test.build_model(load_weights=False)

sr_resnet_test.model.summary()