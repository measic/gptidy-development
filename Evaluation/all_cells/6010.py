scale = sd(train$y)
center = mean(train$y)
train$y = (train$y - center)/scale
test$y = (test$y - center)/scale