# -------------prior and posterior density plot -----------------#
density_plot <- function(alpha_A, beta_A , alpha_B, beta_B , alpha_0, beta_0 ){
        theta<-seq(0,1,0.001) #create theta range from 0 to 1
        prior <- dbeta(theta, alpha_0, beta_0)
        posterior_A <- dbeta(theta, alpha_A, beta_A ) 
        posterior_B <- dbeta(theta, alpha_B, beta_B )

        min_prob = min(   min(posterior_A), min(posterior_B))
        max_prob = max( max(posterior_A), max(posterior_B))
    
        # prior 
        prob_plot <- plot(theta, prior,  col="gray", type= 'l', lty=1, lwd = 2, 
                      xlab = 'Proportion', ylab = "Density",   ylim = c(min_prob ,max_prob),
                         main = "Prior and Posterior Densitys")
        #polygon( c(0,  theta, 1),  c( 0,prior,0,  ),  col= makeTransparent("grey") , border=NA)
    
        # posterior of theta_A , theta_B
        lines(theta, posterior_A, lwd = 2, col="dodgerblue", lty=1)
        polygon( theta  ,  posterior_A,  col= makeTransparent("dodgerblue") , border=NA)
    
        lines(theta, posterior_B, lwd = 2, col="orange", lty=1)
        polygon( theta  ,  posterior_B,  col= makeTransparent("orange") , border=NA)
    
        # Add posterior mean
        abline( v = alpha_A/(alpha_A + beta_A), lty= 1, lwd=2, col= makeTransparent("dodgerblue") )
        abline( v = alpha_B/(alpha_B + beta_B) , lty= 1, lwd=2, col= makeTransparent("orange") )
    
        # Add legend to plot:
        legend("topright",lwd=2, lty= 1 ,
           legend= c("prior", "posterior_A","posterior_B"),
           col = c( "grey","dodgerblue","orange")
           )    
}