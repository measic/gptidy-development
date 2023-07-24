class BucketDataIterator():
    """ Iterator for feeding seq2seq model during training """
    def __init__(self,
                 images,
                 targets,
                 num_buckets=5,
                 train=True):
        
        self.train = train
        length = [len(seq) for seq in images]  

        # Create pandas dataFrame and sort it by images seq lenght (length) 
        # in_length == out_length
        self.dataFrame = pd.DataFrame({'length': length,
                                       'images': images,
                                       'targets': targets
                                      }).sort_values('length').reset_index(drop=True)

        bsize = int(len(images) / num_buckets)
        self.num_buckets = num_buckets
        
        # Create buckets by slicing parts by indexes
        self.buckets = []
        for bucket in range(num_buckets-1):
            self.buckets.append(self.dataFrame.iloc[bucket * bsize: (bucket+1) * bsize])
        self.buckets.append(self.dataFrame.iloc[(num_buckets-1) * bsize:])        
        
        self.buckets_size = [len(bucket) for bucket in self.buckets]

        # cursor[i] will be the cursor for the ith bucket
        self.cursor = np.array([0] * num_buckets)
        self.bucket_order = np.random.permutation(num_buckets)
        self.bucket_cursor = 0
        self.shuffle()
        print("Iterator created.")


    def shuffle(self, idx=None):
        """ Shuffle idx bucket or each bucket separately """
        for i in [idx] if idx is not None else range(self.num_buckets):
            self.buckets[i] = self.buckets[i].sample(frac=1).reset_index(drop=True)
            self.cursor[i] = 0


    def next_batch(self, batch_size):
        """
        Creates next training batch of size: batch_size
        Retruns: image seq, letter seq, seq lengths
        """
        i_bucket = self.bucket_order[self.bucket_cursor]
        # Increment cursor and shuffle in case of new round
        self.bucket_cursor = (self.bucket_cursor + 1) % self.num_buckets
        if self.bucket_cursor == 0:
            self.bucket_order = np.random.permutation(self.num_buckets)
            
        if self.cursor[i_bucket] + batch_size > self.buckets_size[i_bucket]:
            self.shuffle(i_bucket)

        # Handle too big batch sizes
        if (batch_size > self.buckets_size[i_bucket]):
            batch_size = self.buckets_size[i_bucket]

        res = self.buckets[i_bucket].iloc[self.cursor[i_bucket]:
                                          self.cursor[i_bucket]+batch_size]
        self.cursor[i_bucket] += batch_size

        # PAD input sequence and output
        # Pad sequences with <PAD> to same length
        max_length = max(res['length'])
        
        input_seq = np.zeros((batch_size, max_length, N_INPUT), dtype=np.float32)
        for i, img in enumerate(res['images']):
            input_seq[i][:res['length'].values[i]] = img
        
        # Need to pad according to the maximum length output sequence
        targets = np.ones([batch_size, max_length], dtype=np.float32) * PAD
        for i, target in enumerate(targets):
            target[:res['length'].values[i]] = res['targets'].values[i]
        
        return input_seq, targets, res['length'].values


    def next_feed(self, size):
        """ Create feed directly for model training """
        (inputs_,
         targets_,
         length_) = self.next_batch(size)
        return {
            inputs: inputs_,            
            targets: targets_,
            length: length_,
            keep_prob: (1.0 - dropout) if self.train else 1.0
        }