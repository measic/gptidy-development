Bayes_AB_test <- function(nA, xA, nB, xB, 
                          out_data = TRUE, diff_plot= FALSE, 
                          bestProb_plot= FALSE, density_plot=FALSE, 
                          alpha_0= 1, beta_0= 1,  # set both prior parameters to 1 by default
                          digit =3  , nsim =100000, a = Conf_alpha,
                          calculate_CI = TRUE  ){ 
    
   # Conversion rate and uplift
    CR_A = xA/nA*100
    CR_B = xB/nB*100   
    uplift_B = (CR_B- CR_A)/CR_A *100
    
    #-------------------------------------------------------------------        
    # The posterior beta-distritubion of theta_A and theta_B
    alpha_A = alpha_0 + xA
    alpha_B = alpha_0 + xB  
    beta_A  = beta_0 + nA-xA
    beta_B  = beta_0 + nB-xB

    #-------------------------------------------------------------------   
    # If we want to get credible interval of change, need to do simulation, 
    # asumming the two proportions are independent:
    if (calculate_CI == TRUE){
        # simulate theta0 and theta1
        theta0 = rbeta(n= nsim, shape1 = alpha_A, shape2 =beta_A)
        theta1 = rbeta(n= nsim, shape1 = alpha_B, shape2 =beta_B) 
        # compute the difference
        change = theta1 - theta0
        
        # mean_change = mean(change)
        # assuming indepence, the theoretical expectation of change is:
        mean_change = alpha_B/(alpha_B + beta_B) - alpha_A/(alpha_A + beta_A)
        
        # compute equal-tailed (1-alpha) Credible Interval         
        Cred_LL   <- quantile(change , a/2 )
        Cred_UL   <- quantile(change , 1- a/2 )
    }
    else {Cred_LL = NA; Cred_UL = NA}

    #-------------------------------------------------------------------    
    # compute frequentis p-value using Fisher's exact method: 
    mat = matrix(c(xA, nA-xA, xB, nB-xB), nrow = 2 ) 
    p_value = fisher.test( mat , alternative = "two.sided")$p.value
    
    # Compute Bayese Factor using a function from BayesFactor library: 
    BF = as.numeric(as.vector( contingencyTableBF( mat , sampleType = "indepMulti", fixedMargin = "cols")))

    # Probablity of being better can be derived from BF: 
    best_B = prob_B_beats_A(alpha_A, beta_A, alpha_B, beta_B) *100
    best_A = 100 - best_B
    
    #-------------------------------------------------------------------
    # combine and save to result
    result= rbind(c("A", nA, xA, round(CR_A, digits = digit) , 
                    NA, NA, NA, round(best_A, digits = digit),  NA, NA ) ,
                  
                  c("B", nB, xB, round(CR_B, digits = digit) ,  
                    round(uplift_B, digits = digit), 
                    round(mean_change, digits= digit),
                    paste0("(", round(max(0,Cred_LL*100), digits= digit), ", ", 
                           round(min( Cred_UL*100, 100), digits = digit), ")"), 
                    round(best_B, digits = digit), 
                    round(log(BF), digits = digit),

                     round( p_value, digits=digit ) ) )
    
    colnames(result) = c('Test', 'Users', 'Conversion','Conv Rate (%))', 
                         'Uplift (%)', 'Posterior mean of change','Credible Interval',
                         'Chance of being better(%)',
                         'log Bayes Factor', 
                          'frequentist p-value')
    #-------------------------------------------------------------------
    
    if (density_plot ==TRUE){
        density_plot(alpha_A, beta_A , alpha_B, beta_B , alpha_0, beta_0)
    }
    if (bestProb_plot ==TRUE){
        bestProb_plot(round(best_A, digits= digit) , round(best_B, digits= digit) )
    }
    if (calculate_CI == TRUE & diff_plot == TRUE ){
        posterior_plot(change, mean_change, Cred_LL, Cred_UL)
    }
    if(out_data ==TRUE) {return (result)}

}