from keras.callbacks import ModelCheckpoint 
from keras.callbacks import ReduceLROnPlateau

### TODO: specify the number of epochs that you would like to use to train the model.

BATCH_SIZE = 32
epochs = 8

### Do NOT modify the code below this line.

checkpointer = ModelCheckpoint(filepath='saved_models/weights.best.from_scratch.hdf5', 
                               verbose=1, save_best_only=True)

# reduce LR
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2,
                              patience=3, min_lr=0.0005, verbose=1)

augment_data = False   # change to True as needed

if not augment_data:

    print('Training... without data augmentation')
    history = scratch_model.fit(train_tensors, train_targets, 
          validation_data=(valid_tensors, valid_targets),
          epochs=epochs, 
          batch_size=BATCH_SIZE, 
          callbacks=[checkpointer], 
          verbose=1)

else:
    print('Training... WITH data augmentation')
    history = scratch_model.fit_generator(datagen_train.flow(train_tensors, train_targets, batch_size=BATCH_SIZE),
                    steps_per_epoch=train_tensors.shape[0] // BATCH_SIZE,
                    epochs=epochs, 
                    verbose=2, 
                    callbacks=[checkpointer],
                    validation_data=datagen_valid.flow(valid_tensors, valid_targets, batch_size=BATCH_SIZE),
                    validation_steps=valid_tensors.shape[0] // BATCH_SIZE)

print('Done training')
show_history_graph(history)