#Plot visualized correlation matrix
def plot_corr(data,size=20):
    corr = data.corr()
    fig, ax = plt.subplots(figsize=(25, 25))
    cax = ax.matshow(corr)
    fig.colorbar(cax)
    plt.xticks(range(len(corr.columns)), corr.columns,rotation='vertical');
    plt.yticks(range(len(corr.columns)), corr.columns);
    plt.show()
plot_corr(data2)