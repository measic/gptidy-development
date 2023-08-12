from keras.layers import Input
from keras.models import Model
from keras.optimizers import Adam
from keras.preprocessing.image import ImageDataGenerator

import sys
sys.path.append("..")

#import models
from loss import PSNRLoss, psnr

import os
import time
import numpy as np
from imageio import imwrite as imsave
from scipy.misc import imresize
from scipy.ndimage.filters import gaussian_filter

base_weights_path = "weights/"
base_val_images_path = "val_images/"
base_test_images = "test_images/"

set5_path = "tests/set5"
set14_path = "tests/set14"
bsd100_path = "tests/bsd100"

if not os.path.exists(base_weights_path):
    os.makedirs(base_weights_path)

if not os.path.exists(base_val_images_path):
    os.makedirs(base_val_images_path)

if not os.path.exists(base_test_images):
    os.makedirs(base_test_images)

def test_set5(model : Model, img_width=32, img_height=32, batch_size=1):
    datagen = ImageDataGenerator(rescale=1. / 255)
    large_img_width = img_width * 4
    large_img_height = img_height * 4

    iteration = 0
    total_psnr = 0.0

    print("Testing model on Set 5 Validation images")
    total_psnr = _test_loop(set5_path, batch_size, datagen, img_height, img_width, iteration, large_img_height, large_img_width,
                            model, total_psnr, "Set5", 5)

    print("Average PSNR of Set5 validation images : ", total_psnr / 5)
    print()


def test_set14(model : Model, img_width=32, img_height=32, batch_size=1):
    datagen = ImageDataGenerator(rescale=1. / 255)
    large_img_width = img_width * 4
    large_img_height = img_height * 4

    iteration = 0
    total_psnr = 0.0

    print("Testing model on Set 14 Validation images")
    total_psnr = _test_loop(set14_path, batch_size, datagen, img_height, img_width, iteration, large_img_height,
                            large_img_width, model, total_psnr, "Set14", 14)

    print("Average PSNR of Set5 validation images : ", total_psnr / 14)
    print()

def test_bsd100(model : Model, img_width=32, img_height=32, batch_size=1):
    datagen = ImageDataGenerator(rescale=1. / 255)
    large_img_width = img_width * 4
    large_img_height = img_height * 4

    iteration = 0
    total_psnr = 0.0

    print("Testing model on BSD 100 Validation images")
    total_psnr = _test_loop(bsd100_path, batch_size, datagen, img_height, img_width, iteration, large_img_height, large_img_width,
                            model, total_psnr, "bsd100", 100)

    print("Average PSNR of BSD100 validation images : ", total_psnr / 100)
    print()


def _test_loop(path, batch_size, datagen, img_height, img_width, iteration, large_img_height, large_img_width, model,
               total_psnr, prefix, num_images):
    print("Path " + path)
    print("Height " + str(img_height))
    print("img_width " + str(img_width))
    print("large_img_height " + str(large_img_height))
    print("large_img_width " + str(large_img_width))
    print("num_images " + str(num_images))
    for x in datagen.flow_from_directory(path, class_mode=None, batch_size=batch_size,
                                         target_size=(large_img_width, large_img_height)):
        t1 = time.time()

        # resize images
        x_temp = x.copy()
        x_temp = x_temp.transpose((0, 2, 3, 1))

        x_generator = np.empty((batch_size, img_width, img_height, 3))

        for j in range(batch_size):
            img = imresize(x_temp[j], (img_width, img_height))
            x_generator[j, :, :, :] = img

        #x_generator = x_generator.transpose((0, 3, 1, 2))

        output_image_batch = model.predict_on_batch(x_generator)

        average_psnr = 0.0
        for x_i in range(batch_size):
            average_psnr += psnr(x[x_i], output_image_batch[x_i] / 255.)
            total_psnr += average_psnr

        average_psnr /= batch_size

        iteration += batch_size
        t2 = time.time()

        print("Time required : %0.2f. Average validation PSNR over %d samples = %0.2f" %
              (t2 - t1, batch_size, average_psnr))

        for x_i in range(batch_size):
            real_path = base_test_images + prefix + "_iteration_%d_num_%d_real_.png" % (iteration, x_i + 1)
            generated_path = base_test_images + prefix + "_iteration_%d_num_%d_generated.png" % (iteration, x_i + 1)

            val_x = x[x_i].copy() * 255.
            #val_x = val_x.transpose((1, 2, 0))
            val_x = np.clip(val_x, 0, 255).astype('uint8')

            output_image = output_image_batch[x_i]
            #output_image = output_image.transpose((1, 2, 0))
            output_image = np.clip(output_image, 0, 255).astype('uint8')
            
            imsave(real_path, val_x[:,:,0])
            imsave(generated_path, output_image[:,:,0])

        if iteration >= num_images:
            break
    return total_psnr