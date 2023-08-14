oi = np.random.randint(0,n_train)
orig_img = X_train[oi]

fig = plt.figure(figsize=(2,2))
fig.add_subplot(1,1,1)
plt.imshow(X_train[oi])
plt.axis('off')
plt.title('original image', fontsize=10)

fig = plt.figure(figsize=(8,8))
for i in range(5):
    fig.add_subplot(1,5,i+1)
    new_image = transform_image(orig_img,20,10,5)
    plt.imshow(new_image)
    plt.axis('off')

fig.suptitle('5 augmented images:', x=0.5,y=0.6, fontsize=10)
plt.tight_layout()
plt.show()
    
