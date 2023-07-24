Freq_plot <- function(CR, num_tests=2,  Bayes = TRUE)  
{
     # if Bayes== TRUE, plot Bayesian estimate and Credible Interval 
    if (Bayes== TRUE){column = 'Post_mean'; LL = 'Cred_LL' ; UL = 'Cred_UL'; 
                      title= "Bayesian: Posterior Mean and Credible Interval of Proportion Over Time" }
    if (Bayes== FALSE) {column = 'CRate';   LL = 'Conf_LL' ; UL = 'Conf_UL'; 
                      title= "Frequentist: Mean and Confidence Interval of Proportion Over Time" }
    
    #-------------------------Set plot color ----------------------------
    cbPalette <- c("#009E73","#0072B2", "#E69F00",   "#D55E00", "#CC79A7","#F0E442","#56B4E9",  "#999999")
    fill_colors = makeTransparent(cbPalette)
    #------------------------Plot settings:---------------------------------
    # compute the upper and lower bound of y-axis to be 20% and 80% quantile of the upper and lower bound
    min_val  = min( quantile( CR$Cred_LL, 0.01 ), quantile( CR$Conf_LL, 0.01 ))
    max_val  = max( quantile( CR$Cred_UL, 0.99 ), quantile( CR$Conf_UL, 0.01 ))
    max_days = quantile(CR$Day, 0.8)  # x-axis position to put legend
    
    #-------------------------------------------------------------------------    
    data = CR[CR[,'Test_group']==0,]       
    p <- plot(  data[,'Day'],  data[, column] ,type = "l", lwd = 3, col="red", lty=1 , ylim = c(min_val ,max_val) ,
        main = title, 
        xlab = 'Days after tests start' , ylab= 'Proportion')
    polygon( c(data[,'Day'] , rev(data[,'Day']) ), c(data[, LL] , rev(data[, UL]) ), 
            col=rgb(1, 0, 0,0.1), border=NA)
    #-------------------------------------------------------------------------    
    abline(h=0)
    # plot the rest test groups
    for (k in 1:num_tests){
        data = CR[CR[,'Test_group']==k,]
        lines(  data[,'Day'],  data[, column] ,type = "l", lwd = 3, col= cbPalette[k], lty=k+1   )
        polygon( c(data[,'Day'] , rev(data[,'Day']) ), c(data[,LL] , rev(data[, UL]) ), 
                col= fill_colors[k], border=NA)
        }
    #-------------------------------------------------------------------------        
    # add legend to the plot
    legend_list = c()
    for (k in 1:num_tests){ legend_list = c(legend_list,  paste0("Test ", k) )}
    legend( max_days , max_val, legend= legend_list, 
       col=c("red", cbPalette[2:k]), lty=1:(k+1), cex=0.8, title="Test group")
    }