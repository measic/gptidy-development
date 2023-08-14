epochs = 200
batch_size = 128
n_samples_train = 4096
n_samples_valid = 1024
status_update_every = 20

x_valid, y_valid = msig.generate_samples(n_samples_valid, 'tf_tc')

training_generator = SignalGenerator(n_samples_train, batch_size, msig, 'tf_tc')
t0 = time.time()
model.fit_generator(
    generator=training_generator,
    validation_data=(x_valid, y_valid),
    verbose=1, 
    epochs=epochs,
    callbacks=[
        csvlogger,
        checkpointer
    ],
    use_multiprocessing=True,
    workers=4
)
if (i + 1) % status_update_every == 0:
    print('#' * 45)
    print(f'Epoch: {(i + 1)}/{epochs}, Time: {time.time() - t0}')
    print('#' * 45)
    t0 = time.time()