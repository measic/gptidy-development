%%time

def train(epochs, logstep, lr):
    print("Running {} epochs with learning rate {}".format(epochs, lr))
    for i in range(epochs):
        _, s = sess.run([update, merged_summary], feed_dict={learning_rate: lr, max_global_norm: 5.0})
        l = sess.run(loss)
        writer.add_summary(s, i)
        if i % logstep == logstep - 1:
            print("Iter {}, learning rate {}, loss {}".format(i+1, lr, l))
            
print("Start training...")
if use_toy_data:
    train(100, 10, .5)
else:
    train(350, 50, 1)
    train(1000, 100, 0.1)
    train(1000, 100, 0.01)