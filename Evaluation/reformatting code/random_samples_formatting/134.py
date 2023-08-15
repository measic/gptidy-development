#ignore
# google drive sync

save_to_gdrive = True
dataset_in_gdrive = False # set to True for speed up without training


if save_to_gdrive:
  from google.colab import drive
  drive.mount('/content/gdrive')
  output_dir = os.path.join("/content/gdrive/My Drive", output_dir)
    
en_vocab_file = os.path.join(output_dir, "en_vocab")
zh_vocab_file = os.path.join(output_dir, "zh_vocab")
checkpoint_path = os.path.join(output_dir, "checkpoints")
log_dir = os.path.join(output_dir, 'logs')

if dataset_in_gdrive:
  download_dir = os.path.join(output_dir, "tensorflow-datasets/downloads")
else:
  download_dir = "tensorflow-datasets/downloads"
    
# print(f"Save result to {output_dir}")
clear_output()