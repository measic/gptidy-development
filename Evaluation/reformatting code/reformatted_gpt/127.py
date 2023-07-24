plot_change_column <- function(CR_change, num_tests=3, variable, var_label, 
                               hline=0, plot_min_pct=0.01, plot_max_pct=0.99,
                               legend_position="right"):
    # Set color for plot
    cbPalette <- c("#009E73", "#0072B2", "#E69F00", "#D55E00", "#CC79A7", "#F0E442", "#56B4E9", "#999999")
    fill_colors = makeTransparent(cbPalette)
    
    # Plot settings:
    # compute the upper and lower bound of y-axis to be 20% and 80% quantile of the upper and lower bound
    min_val = quantile(CR_change[, variable], plot_min_pct)
    max_val = max(CR_change[, variable])  
    
    # Plot the first group
    data = CR_change[CR_change[,'Test_group'] == 1, ] 
    plot(data[,'Day'], data[, variable], type="l", lwd=3, col=cbPalette[1], lty=1, ylim=c(min_val, max_val),
         main=paste0("Trend of ", var_label, " Over Time"), xlab=var_label, ylab='Percent')
    
    # Plot the other groups
    for (k in 2:num_tests):
        data = CR_change[CR_change[,'Test_group'] == k, ] 
        lines(data[,'Day'], data[, variable], type="l", lwd=3, col=cbPalette[k], lty=k+1)
    
    abline(h=hline)
    
    # Add legend to the plot
    legend_list = c()
    for (k in 1:num_tests):
        legend_list = c(legend_list, paste0("Test ", k))
    legend(legend_position, legend=legend_list, col=c(cbPalette[1:k]), lty=1:(k+1), cex=0.8, title="Test group")