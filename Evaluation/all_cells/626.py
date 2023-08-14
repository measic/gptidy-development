# Create iterator for feeding BiRNN
train_iterator = BucketDataIterator(trainImages,
                                    trainLabels,
                                    num_buckets,
                                    train=True)
test_iterator = BucketDataIterator(testImages,
                                   testLabels,
                                   1,
                                   train=False)