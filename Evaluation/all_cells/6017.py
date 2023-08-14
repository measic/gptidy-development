resid_plot = function(df, score){
    df$score = score
    df$resids = df$y - score
    ggplot(df, aes(score, resids)) + 
    geom_point() + 
    ggtitle('Residuals vs. Predicted Values') +
    xlab('Predicted values') + ylab('Residuals')
}

resid_plot(test, score)