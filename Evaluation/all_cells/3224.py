balls = make_random_balls(num_balls = num_examples, im_shape = im_shape)

fig = figure(0, (12,12))
for i, ball in enumerate(balls):
    if i < 9:
        fig.add_subplot(3, 3, i + 1)
        imshow(ball, cmap = 'gray')