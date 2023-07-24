### TODO: Train the model.

EPOCHS = 20
BATCH_SIZE=16

from keras.callbacks import ReduceLROnPlateau

# checkpoint file
inception_ckpoint_file = 'saved_models/inceptionv3_bneck.weights.hdf5'
## callbacks
checkpointer = ModelCheckpoint(filepath=inception_ckpoint_file, 
                               verbose=1, save_best_only=True)


# reduce LR
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                              patience=5, min_lr=0.0005, verbose=1)

print('Starting training...')
hist = inception_bneck.fit(train_incp_bn, train_targets,
                          validation_data=(valid_incp_bn, valid_targets),
                          epochs=EPOCHS,
                          batch_size=BATCH_SIZE,
                          callbacks=[checkpointer, reduce_lr],
                          verbose=1)
print('Training done.')
# plot the history
show_history_graph(hist)