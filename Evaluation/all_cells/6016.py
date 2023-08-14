resids_qq = function(df, score, bins = 10){
    options(repr.plot.width=4, repr.plot.height=3.5) # Set the initial plot area dimensions
    df$resids = df$y - score
    ggplot() + 
    geom_qq(data = df, aes(sample = resids)) + 
    stat_qq_line(data = df, aes(sample = resids)) +
    ylab('Quantiles of residuals') + xlab('Quantiles of standard Normal') +
    ggtitle('QQ plot of residual values')
}

resids_qq(test, score)