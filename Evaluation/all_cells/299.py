# The fomulas provided by http://www.evanmiller.org/bayesian-ab-testing.html went wrong then n is very large
# need to get this from simulation: 

prob_B_beats_A = function(alpha_A, beta_A, alpha_B, beta_B){
    total = 0.0
    for (i in 0:(alpha_B-1)){
        total = total + exp(lbeta(alpha_A + i, beta_B + beta_A) 
            - log(beta_B + i) - lbeta(1 + i, beta_B) - lbeta(alpha_A, beta_A))
    }
    return(total)
}

# A/B/C testing: binary outcomes
probability_C_beats_A_and_B <- function(alpha_A, beta_A, alpha_B, beta_B, alpha_C, beta_C){
    total = 0.0
    for (i in 0:(alpha_A-1) ){
        for (j in 0:(alpha_B-1)){
            total = total + exp(lbeta(alpha_C+i+j, alpha_A+alpha_B+alpha_C) 
                                - log(alpha_A+i) - log(alpha_B+j))
        }        
    }         
    return (1 - probability_B_beats_A(alpha_C, alpha_C, alpha_A, alpha_A)  
            - probability_B_beats_A(alpha_C, alpha_C, alpha_B, alpha_B) + total )    
}
