# all the subbasins in the hydrologic partition (including virtual stations)
#gcs_get_dir('pangeo-data/gross/ws_mask/amazonas', 'ws_mask/amazonas', fs)
#gcs_w_token = gcsfs.GCSFileSystem(project='pangeo-data', token='browser')
if is_pangeo_data:
    fs = gcsfs.GCSFileSystem(project='pangeo-data')
    all_labels = [os.path.basename(path[:-1]) for path in fs.ls('pangeo-data/gross/ws_mask/amazonas') if os.path.basename(path[:-1]).startswith('0')]
else:
    all_labels = [fname for fname in os.listdir('ws_mask/amazonas') if fname.startswith('0')]
print('Total number of subbasins:', len(all_labels))