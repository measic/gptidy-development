fig = figure(0, (8,6))
scatter(X[:,0], X[:,1], c = y, s = 75)
xlabel('$x_1$', fontsize = 20)
ylabel('$x_2$', fontsize = 20)
xlim([0, 6]); ylim([0, 4])
grid(1)