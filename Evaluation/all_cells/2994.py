csvlogger = CSVLogger(msig.training_stats_filename, separator=',', append=True)
checkpointer = ModelCheckpoint(msig.model_filename, save_best_only=True, save_weights_only=False, verbose=1, period=5)