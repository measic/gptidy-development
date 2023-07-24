hist_resids = function(df, score, bins = 10){
    options(repr.plot.width=4, repr.plot.height=3) # Set the initial plot area dimensions
    df$resids = df$y - score
    bw = (max(df$resids) - min(df$resids))/(bins + 1)
    ggplot(df, aes(resids)) + 
       geom_histogram(binwidth = bw, aes(y=..density..), alpha = 0.5) +
       geom_density(aes(y=..density..), color = 'blue') +
    xlab('Residual value') + ggtitle('Histogram of residuals')
}

hist_resids(test, score)