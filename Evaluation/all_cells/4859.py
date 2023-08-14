plt.figure(figsize = (20,10))
ax = plt.gca()
ax.scatter(tsne_embedded[:,0],tsne_embedded[:,1], s=20)

for i, txt in enumerate(most_freq_words):
    ax.annotate(txt, (tsne_embedded[i]))
    
condi_circle = plt.Circle((10,10),1,alpha=0.25, color="orange")
do_circle = plt.Circle((6.7,11),1,alpha=0.25, color="blue")
like_circle = plt.Circle((1,5.5), 1,alpha=0.25, color="red")
great_circle = plt.Circle((-3.5,-9.5), 1,alpha=0.25, color="green")

ax.add_artist(condi_circle)
ax.add_artist(do_circle)
ax.add_artist(like_circle)
ax.add_artist(great_circle)
plt.show()