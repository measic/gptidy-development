# A function to do data manipulation

transform_data <- function(df, a = Conf_alpha, a_0 = alpha_0, b_0 = beta_0) {
    num_tests = length(unique(df$Test_group)) - 1

    result = data.frame()
    for (k in 0:num_tests) {
        df_k = df[df$Test_group == k, ]
        data = as.data.frame.matrix(table(df_k$Date, df_k$Convert))
        data[, 1] = data[, 1] + data[, 2]  # change the first column from not convert to total counts

        Date = rownames(data)  # row name to Date
        Day = as.numeric(as.Date(Date) - min(as.Date(Date)) + 1)  # Compute date from start
        data = cbind(Date, Day, k, data)  # add to data
        rownames(data) <- NULL
        colnames(data) <- c("Date", "Day", "Test_group", "Total", "Convert")

        # calculate the cumulated clicked and cumulated converted
        data$Cum_Total = cumsum(data$Total)
        data$Cum_Convert = cumsum(data$Convert)
        data$CRate = data$Cum_Convert / data$Cum_Total

        ## Upper and lower limit of frequentist confidence interval
        data$Conf_LL = data$CRate - qnorm(1 - a / 2, mean = 0, sd = 1) * sqrt(data$CRate * (1 - data$CRate) / data$Cum_Total)
        data$Conf_UL = data$CRate + qnorm(1 - a / 2, mean = 0, sd = 1) * sqrt(data$CRate * (1 - data$CRate) / data$Cum_Total)
        data$Conf_LL = as.numeric(lapply(data$Conf_LL, function(x) max(0, x)))
        data$Conf_UL = as.numeric(lapply(data$Conf_UL, function(x) min(1, x)))

        ## Summaries based on posterior probability
        post_alpha = a_0 + data$Cum_Convert
        post_beta = b_0 + data$Cum_Total - data$Cum_Convert
        data$Post_mean = (post_alpha) / (post_alpha + post_beta)

        # compute equal-tailed credible interval for the posterior Beta distribution
        data$Cred_LL = qbeta(a / 2, shape1 = post_alpha, shape2 = post_beta)
        data$Cred_UL = qbeta(1 - a / 2, shape1 = post_alpha, shape2 = post_beta)
        data$Cred_LL = as.numeric(lapply(data$Cred_LL, function(x) max(0, x)))
        data$Cred_UL = as.numeric(lapply(data$Cred_UL, function(x) min(1, x)))

        # save the data set to result
        if (dim(result)[1] > 0) {
            result = rbind(result, data)
        } else {
            result = data
        }
    }
    return(result)
}