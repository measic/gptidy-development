# Test with the test_images subdirs
for graph in (output_graph_orig, output_graph):
    print("\nTesting with graph=%s\n" % graph)
    for subdir in ('house_with_pool', 'house_without_pool'):
        test_dir = os.path.join(test_images_dir, subdir)
        for f in os.listdir(test_dir):
            if f.endswith(JPEG_EXTENSIONS):
                tf.reset_default_graph()
                image = os.path.join(test_dir, f)
                print(image)
                %run ../image_retraining/label_image.py --image=$image --graph=$graph --labels=$output_labels