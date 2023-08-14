print_metrics = function(lin_mod, df, score){
    resids = df$y - score
    resids2 = resids**2
    N = length(score)
    r2 = as.character(round(summary(lin_mod)$r.squared, 4))
    adj_r2 = as.character(round(summary(lin_mod)$adj.r.squared, 4))
    cat(paste('Mean Square Error      = ', as.character(round(sum(resids2)/N, 4)), '\n'))
    cat(paste('Root Mean Square Error = ', as.character(round(sqrt(sum(resids2)/N), 4)), '\n'))
    cat(paste('Mean Absolute Error    = ', as.character(round(sum(abs(resids))/N, 4)), '\n'))
    cat(paste('Median Absolute Error  = ', as.character(round(median(abs(resids)), 4)), '\n'))
    cat(paste('R^2                    = ', r2, '\n'))
    cat(paste('Adjusted R^2           = ', adj_r2, '\n'))
}

print_metrics(lin_mod, test, score)          