set.seed(9988)
test_idx <- sample(seq_len(nrow(df)), size = 50)

train <- df[test_idx, ] # Select the training rows
test <- df[-test_idx, ] # Select the test rows
dim(train)
dim(test)