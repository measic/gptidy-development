plot_regression = function(score, df){
    df$score = score
    ggplot(df) + geom_point(aes(x,y)) +
                 geom_line(aes(x,score), color = 'red', size = 1) +
                 ggtitle('Regression of X vs. Y')
}

score = predict(lin_mod, newdata = test)
plot_regression(score, test)