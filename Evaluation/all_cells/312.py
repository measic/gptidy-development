Change_plot <- function(CR_change, Bayes = TRUE)  
{
    num_tests = length(unique( CR_change[,'Test_group'])) 
    
    # if Bayes== TRUE, plot Bayesian estimate and Credible Interval 
    if (Bayes== TRUE){column = 'Post_mean'; LL = 'Cred_LL' ; UL = 'Cred_UL'; 
                      title= "Bayesian: Posterior Mean and Credible Interval of Change Over Time" }
    else{        column = 'CRate_change';   LL = 'Conf_LL' ; UL = 'Conf_UL'; 
                      title= "Frequentist: Mean and Confidence Interval of Change Over Time" }
    
    #-------------- Set color for plot ------------------------------
    cbPalette <- c("#009E73","#0072B2", "#E69F00",   "#D55E00", "#CC79A7","#F0E442","#56B4E9",  "#999999")
    fill_colors = makeTransparent(cbPalette)
    #-------------------------------------------------------------------------
    # Plot settings:
    # compute the upper and lower bound of y-axis to be 20% and 80% quantile of the upper and lower bound
    min_val = min( quantile(CR_change[, 'Cred_LL'], 0.01 ), quantile(CR_change[, 'Conf_LL'], 0.01 ))
    max_val = max( quantile(CR_change[, 'Cred_UL'], 0.99 ), quantile(CR_change[, 'Conf_UL'], 0.01 ))
    max_days = quantile(CR_change[,'Day'], 0.8)  # x-axis position to put legend
    
    # -------------- plot the first group -------------- 
    data =  CR_change[CR_change[,'Test_group'] == 1, ] 
    
    plot(  data[,'Day'],  data[, column] ,type = "l", lwd = 3, col= cbPalette[1], lty=1 , ylim = c(min_val, max_val) ,
        main = title, 
        xlab = 'Days after tests start' , ylab= 'Proportion')
    polygon( c(data[,'Day'] , rev(data[,'Day']) ), c(data[, LL] , rev(data[, UL]) ), 
            col= fill_colors[1], border=NA)

    # -------------- plot the other groups-------------- 
    for (k in 2:num_tests){
        data = CR_change[CR_change[,'Test_group'] == k, ]
        lines(  data[,'Day'],  data[, column] ,type = "l", lwd = 3, col= cbPalette[k], lty=k+1   )
        polygon( c(data[,'Day'] , rev(data[,'Day']) ), c(data[,LL] , rev(data[, UL]) ), 
                col= fill_colors[k], border=NA)
        }
    abline(h=0)
    
    #------------------add legend to the plot -----------------
    legend_list = c()
    for (k in 1:num_tests){ legend_list = c(legend_list,  paste0("Test ", k) )}
    legend( max_days , max_val, legend= legend_list, 
       col=c( cbPalette[1:k]), lty=1:(k+1), cex=0.8, title="Test group")

}
