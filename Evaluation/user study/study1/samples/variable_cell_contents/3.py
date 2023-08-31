def plot(embeddings, labels):
    assert embeddings.shape[0] >= len(labels), 'More labels than embeddings'
    pylab.figure(figsize=(15, 15))
    for i, label in enumerate(labels):
        variable_def, y = embeddings[i, :]
        pylab.scatter(variable_def, y)
        pylab.annotate(label, xy=(variable_def, y), xytext=(5, 2), textcoords='offset points', ha='right', va='bottom')
    pylab.show()
words = [reverse_dictionary[i] for i in range(1, num_points + 1)]
plot(two_d_embeddings, words)