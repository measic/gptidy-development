# -------------Plot posterior density of change -----------------#
posterior_plot <- function(change, mean_change, Cred_LL, Cred_UL){
    d = density(change )
    plot(d, main="Posterior Density of proportion change", col = "#009E73" )
    polygon(d, col='#009E7326', border=NA)
    abline( v = Cred_LL , lty= 3, lwd=2, col= "grey")
    abline( v = Cred_UL , lty= 3, lwd=2, col= "grey")
    abline( v = mean_change , lty= 1, lwd=2, col= "grey")
    
    # add legend 
    legend("topright",lwd=2, lty= c(1,3),
           legend= c("Posterior mean", "Credible Interval"),
           col = c( "grey","grey"),  cex = 0.8
           )  
    ## Add mean and CI value
    print(mean_change)
    text(y = 0,  x = mean_change, label = round(mean_change, digits=4) , cex = 0.8)
    text(y = 0,  x = Cred_LL, label = round(Cred_LL, digits=4) , cex = 0.8)
    text(y = 0,  x = Cred_UL, label = round(Cred_UL, digits=4) , cex = 0.8)
}        