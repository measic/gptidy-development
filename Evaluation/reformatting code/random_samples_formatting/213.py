# Download the Inception model once and reuse it (set the flag and clobber it each time).
if force_inception_download and os.path.isdir(model_dir):    
    shutil.rmtree(model_dir)
retrain.maybe_download_and_extract()