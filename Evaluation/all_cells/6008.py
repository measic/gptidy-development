set.seed(34567)
df = data.frame(x = seq(from = 0.0, to = 10.0, by = 0.1))
df$y = df$x + rnorm(length(df$x), mean = 0.0, sd = 1.0)

ggplot(df, aes(x,y)) + geom_point()