# Prepare for model:
X2_norm = norm_image(X2)

fig = plt.figure(figsize=(15, 15))
gr = gridspec.GridSpec(1, 6)
for i in range(num_own_examples):
    plt.subplot(1,6,i+1)
    plt.imshow(X2_norm[i].reshape(32,32), cmap = 'gray')
    plt.axis('off')
plt.tight_layout()
fig.suptitle('6 new traffic signs after gray scale and data normalization', x=0.5,y=0.6, fontsize=20)
plt.show()  