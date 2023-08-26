import math
from matplotlib import cm, pyplot as plt, mlab

def visualize(word, model):
    """ visualize the input model for a particular word """
    variance = np.array([np.diag(model.covars_[i]) for i in range(model.n_components)])
    figures = []
    for parm_idx in range(len(model.means_[0])):
        xmin = int(min(model.means_[:, parm_idx]) - max(variance[:, parm_idx]))
        xmax = int(max(model.means_[:, parm_idx]) + max(variance[:, parm_idx]))
        fig, axs = plt.subplots(model.n_components, sharex=True, sharey=False)
        colours = cm.rainbow(np.linspace(0, 1, model.n_components))
        for i, (ax, colour) in enumerate(zip(axs, colours)):
            x = np.linspace(xmin, xmax, 100)
            variable_def = model.means_[i, parm_idx]
            sigma = math.sqrt(np.diag(model.covars_[i])[parm_idx])
            ax.plot(x, mlab.normpdf(x, variable_def, sigma), c=colour)
            ax.set_title('{} feature {} hidden state #{}'.format(word, parm_idx, i))
            ax.grid(True)
        figures.append(plt)
    for p in figures:
        p.show()
visualize(my_testword, model)