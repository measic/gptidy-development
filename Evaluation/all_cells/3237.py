# Use a fresh working dir for the bottleneck files  
if os.path.isdir(bottleneck_dir):    
    shutil.rmtree(bottleneck_dir)
os.mkdir(bottleneck_dir)

subdirs = ('house_with_pool', 'house_without_pool')

# Copy in the stored bottleneck files
for subdir in subdirs:
    dest_dir = os.path.join(bottleneck_dir, subdir)
    if not os.path.isdir(dest_dir):
        os.mkdir(dest_dir)

    image_dest_dir = os.path.join(images_resized_dir, subdir)

    if stored_bottlenecks:
        source_dir = os.path.join(stored_bottlenecks, subdir)
        if os.path.isdir(source_dir):
            for f in os.listdir(source_dir):
                path = os.path.join(source_dir, f)
                if (os.path.isfile(path)):
                    # Copy the persisted bottleneck to bottlenecks dir
                    shutil.copy(path, dest_dir)
                    # "touch" the file (w/o the .txt) to create a placeholder image
                    # This image file will only be used to build the lists.
                    if DEBUG:
                        print("Creating placeholder image at %s" % os.path.join(image_dest_dir, f[:-4]))
                    open(os.path.join(image_dest_dir, f[:-4]), 'a').close
                        