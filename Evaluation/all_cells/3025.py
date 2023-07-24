x_test, y_test = msig.generate()
y_hat, *args = model2.predict(x_test, batch_size=batch_size)
model2.reset_states()
y_pred = np.argmax(y_hat, axis=-1)
print('x_test', x_test.shape, '{:>9.4f} {:>9.4f}'.format(np.min(x_test), np.max(x_test)))
print('y_test', y_test.shape)
print('y_hat ', y_hat.shape, '{:>9.4f} {:>9.4f}'.format(np.min(y_hat), np.max(y_hat)))
print('y_pred', y_pred.shape, '{} {}'.format(np.min(y_pred), np.max(y_pred)))
for i, arg in enumerate(args):
    print(i, arg.shape, '{:>9.4f} {:>9.4f}'.format(np.min(arg), np.max(arg)))