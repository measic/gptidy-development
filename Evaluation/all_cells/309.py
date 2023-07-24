#CR01= Calculate_change(CR, 1)
#CR02= Calculate_change(CR, 2)
#CR03= Calculate_change(CR, 3)
#head(CR01)

Cal_all_change <- function(CR,  Conf_alpha, alpha_0, beta_0 ){
    num_tests = length(unique( CR[,'Test_group'])) -1 
    result= data.frame()
    for (k in 1:num_tests){
        data = Calculate_change(CR, k, Conf_alpha, alpha_0, beta_0)
        # save the data set to result
        if (dim(result)[1] > 0){ result= rbind(result, data)}
        else{result= data}
    }
    return(result)
}