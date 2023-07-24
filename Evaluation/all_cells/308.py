Calculate_change <- function(CR, k , a = Conf_alpha, alpha_0, beta_0, 
                             nsim = 10000, digit= 4){
    
    CR0 =  CR[CR[,'Test_group'] ==0, c('Day','Cum_Total','Cum_Convert',"CRate") ]
    CR1 =  CR[CR[,'Test_group'] ==k, c('Day','Cum_Total','Cum_Convert',"CRate") ]
    CR01= merge(CR0, CR1, by= 'Day', all=TRUE)
    

    CR01 = cbind( k, CR01)
    colnames(CR01) <- c("Test_group","Day", "Total_0","Convert_0", "CRate_0" ,"Total_k","Convert_k", "CRate_k")    

    
    N= dim(CR0)[1]  # total number of days in the study
    
    n0 = CR01$Total_0; x0 = CR01$Convert_0; p0 =  CR01$CRate_0 
    n1 = CR01$Total_k; x1 = CR01$Convert_k; p1 =  CR01$CRate_k 

    
    p_hat = (x0+ x1) /(n0+n1) # pooled estimate of proportion, assuming two groups have equal proportion
    
    ## ----------Upper and lower limit of frequentist confidence interval------------
    z = qnorm(1-a/2, mean = 0, sd = 1) 
    
    CR01$CRate_change = p1- p0
    CR01$Conf_LL =  (p1- p0) - z* sqrt( p_hat*(1-p_hat) *(1/n0 + 1/n1) )
    CR01$Conf_UL =  (p1- p0) + z* sqrt( p_hat*(1-p_hat) *(1/n0 + 1/n1) )
    
    Z_stat = (p1- p0)/ sqrt( p_hat*(1-p_hat) *(1/n0 + 1/n1) )
    # Use normal approximation to calculate p-value
    p_value = (1- pnorm(abs(Z_stat)) )*2 
    
    #--------------------------------------------------------------------------------
    # For each day, simulate posterior distribution of difference p1-p0:
    # And compute Upper and lower limit of Bayesian credible interval----------------

    Post_mean <- c()
    Cred_LL   <- c()
    Cred_UL   <- c()
    logBF     <- c()
    prob_better <- c()
    
    for (i in 1:N){
        # posterior dist parameters: 
        alpha_A = alpha_0 + x0[i]
        alpha_B = alpha_0 + x1[i]  
        beta_A  = beta_0 + n0[i]-x0[i]
        beta_B  = beta_0 + n1[i]-x1[i]
        
        # simulate theta0 and theta1
        theta0 = rbeta(n= nsim, shape1 = alpha_A, shape2 =beta_A)
        theta1 = rbeta(n= nsim, shape1 = alpha_B, shape2 =beta_B) 
        
        # compute the difference
        change = theta1 - theta0
        # compute mean, sd, approximate 1-alpha Credible Interval 
        mean_change = mean(change)
        sd_change   = sd(change)
        Post_mean = c(Post_mean, mean_change)
        Cred_LL   <- c(Cred_LL, mean_change - z * sd_change)
        Cred_UL   <- c(Cred_UL, mean_change + z * sd_change)
        
        prob_better <- c(prob_better, prob_B_beats_A(alpha_A, beta_A, alpha_B, beta_B)*100 )
        
        #-----------Bayes Factors -------------------------------------------
        mat = matrix(c(x0[i], n0[i]-x0[i], x1[i], n1[i]-x1[i]), nrow = 2 ) 
        logBF = c( logBF, log(as.numeric(as.vector( contingencyTableBF( mat , sampleType = "indepMulti", 
                                                  fixedMargin = "cols")))) )
    }
    
    CR01$Post_mean = Post_mean
    CR01$Cred_LL   = Cred_LL
    CR01$Cred_UL   = Cred_UL
    CR01$prob_better= prob_better
    CR01$Uplift    = (p1 - p0)/p0 *100
    CR01$logBF     = logBF
    CR01$p_value   = p_value
    #--------------------------------------------------------------------------------
    CR01 <- CR01[ -c(5,8) ]
    return(CR01)
}