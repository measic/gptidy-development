
simulate_data <- function(num_tests, start_date, test_duration,counts , prob_list,
                          alpha_0, beta_0){
    DF <- data.frame( Test_group = numeric(), Date = as.Date(character()), Convert = numeric())
  for (i in 0:num_tests) {

    data = data.frame( Test_group = i, 
                 Date = sample(seq(start_date, start_date+ test_duration -1 , by="day"), counts, replace = TRUE ), 
                 Convert = rbinom(n = counts, size= 1, prob = prob_list[i+1]))  
    DF <- rbind(DF, data)
  }
  return(DF)
}
DF <- simulate_data(num_tests, start_date, test_duration,counts , 
                    prob_list , alpha_0, beta_0 )
dim(DF)
head(DF)