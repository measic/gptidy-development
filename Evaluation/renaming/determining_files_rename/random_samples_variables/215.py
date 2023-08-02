def plot(embeddings, labels):
    assert embeddings.shape[0] >= len(labels), 'More labels than embeddings'
    pylab.figure(figsize=(15, 15))
    for i, label in enumerate(labels):
        x, variable_def = embeddings[i, :]
        pylab.scatter(x, variable_def)
        pylab.annotate(label, xy=(x, variable_def), xytext=(5, 2), textcoords='offset points', ha='right', va='bottom')
    pylab.show()
words = [reverse_dictionary[i] for i in range(1, num_points + 1)]
plot(two_d_embeddings, words)