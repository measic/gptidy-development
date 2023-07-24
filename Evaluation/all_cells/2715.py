## 'path' can point to a local file, hdfs, s3, nfs, Hive, directories, etc.
df = h2o.import_file(path = "http://s3.amazonaws.com/h2o-public-test-data/smalldata/gbm_test/titanic.csv")
print df.dim
print df.head
print df.tail
print df.describe

## pick a response for the supervised problem
response = "survived"

## the response variable is an integer, we will turn it into a categorical/factor for binary classification
df[response] = df[response].asfactor()           

## use all other columns (except for the name & the response column ("survived")) as predictors
predictors = df.columns
del predictors[1:3]
print predictors