infile = get_dataset_path('gamma_test_large.simtel.gz')   

dl1_parameters_filename = 'dl1.h5'

allowed_tels = {1} # select LST1 only
max_events = 300 # limit the number of events to analyse in files - None if no limit

cal = CameraCalibrator()