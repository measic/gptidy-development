k=1
df = DF
        df_k = df[ df$Test_group == k, ]
        data = as.data.frame.matrix( table(df_k$Date, df_k$Convert))
        data[,1] = data[,1] + data[,2]   # change the first column from not convert to total counts
        
        Date = rownames(data)   #  row name to Date 
        Day = as.numeric( as.Date(Date) - min(as.Date(Date)) +1)  # Compute date from start
        data = cbind(Date, Day, k, data) # add to data
        rownames(data) <- NULL
        colnames(data) <- c("Date", "Day", "Test_group", "Total", "Convert")

head(data)