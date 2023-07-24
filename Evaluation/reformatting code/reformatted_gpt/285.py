n_samples_train = 2048
n_samples_valid = 512
epochs = 200
dump_every = 1
status_update_every = 50

x_valid, y_valid, *_ = msig.generate_samples(n_samples_valid, 'tf_tc')

for i in range(epochs):
    x_train, y_train, *_ = msig.generate_samples(n_samples_train, 'tf_tc')
    model.fit(
        x_train, y_train,
        epochs=1,
        validation_data=(x_valid, y_valid),
        batch_size=batch_size,
        verbose=1,
        callbacks=[
            csvlogger,
            checkpointer
        ],
    )
    if stateful:
        model.reset_states()

    # Code specific to window_type == sliding

    # if (i + 1) % dump_every == 0:
    #     test_dict['epoch'].append(i + 1)
    #     score = model.evaluate(test_dict['X'], test_dict['y'], batch_size=batch_size)
    #     if stateful:
    #         model.reset_states()
    #     test_dict['score'].append(score)

    #     y_hat = model.predict(test_dict['X'], batch_size=batch_size)
    #     if stateful:
    #         model.reset_states()
    #     test_dict['y_hat'].append(y_hat)

    if (i + 1) % status_update_every == 0:
        print('#' * 50)
        print(f'Epoch: {(i + 1)}/{epochs}')
        print('#' * 50)
#         model.save(msig.model_filename)