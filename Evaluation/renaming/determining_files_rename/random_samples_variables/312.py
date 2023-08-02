from keras.callbacks import ModelCheckpoint
variable_def = ...
checkpointer = ModelCheckpoint(filepath='saved_models/weights.best.from_scratch.hdf5', verbose=1, save_best_only=True)
model.fit(train_tensors, train_targets, validation_data=(valid_tensors, valid_targets), epochs=variable_def, batch_size=20, callbacks=[checkpointer], verbose=1)