def resize_images(src_dir, dest_dir):
    if not os.path.isdir(src_dir):
        raise Exception(src_dir + " is not a directory")
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)

    raw_images = {image for image in os.listdir(src_dir) if image.endswith(
        JPEG_EXTENSIONS)}
    dest_images = {image for image in os.listdir(dest_dir)}

    # Resize the ones that are not already in the dest dir
    for image in raw_images - dest_images:
        if DEBUG:
            print("Resizing " + image)
        resize_image(image, src_dir, dest_dir)


def resize_image(image_file, src_dir, dest_dir):
    in_file = os.path.join(src_dir, image_file)
    with open(in_file, 'r+b') as fd_img:
        with Image.open(fd_img) as img:
            resized_image = resizeimage.resize_contain(
                img, [299, 299]).convert("RGB")
            resized_image.save(os.path.join(dest_dir, image_file), img.format)

# Use a fresh working dir for the resized images
if os.path.isdir(images_resized_dir):
    shutil.rmtree(images_resized_dir)
os.mkdir(images_resized_dir)
    
subdirs = ('house_with_pool', 'house_without_pool')

# Copy in the image files
for subdir in subdirs:
    dest_dir = os.path.join(images_resized_dir, subdir)
    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir)
      
    # Copy the already resized files first, if any, from the repo or a custom dir
    if stored_images_resized:
        source_dir = os.path.join(stored_images_resized, subdir)
        if os.path.isdir(source_dir):
            for f in os.listdir(source_dir):
                path = os.path.join(source_dir, f)
                if (os.path.isfile(path)):
                    shutil.copy(path, dest_dir)
                    
    # Copy/resize the remaining raw images into the images_resized_dir(s)
    resize_images(os.path.join(image_dir, subdir), dest_dir)