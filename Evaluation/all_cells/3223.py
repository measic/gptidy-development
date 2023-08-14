bricks = make_random_bricks(num_bricks=num_examples, im_shape = im_shape)

fig = figure(0, (12,12))
for i, brick in enumerate(bricks):
    if i < 9:
        fig.add_subplot(3, 3, i + 1)
        imshow(brick, cmap = 'gray')