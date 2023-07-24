class Dataset(object):
    PAD = 0
    SOS = 1
    EOS = 2
    UNK = 3
    #src_vocab = ['PAD', 'UNK']
    constants = ['PAD', 'SOS', 'EOS', 'UNK']
    hu_alphabet = list("aábcdeéfghiíjklmnoóöőpqrstuúüűvwxyz-+._")
    
    def __init__(self, fn, config, src_alphabet=None, tgt_alphabet=None):
        self.config = config
        self.create_tables(src_alphabet, tgt_alphabet)
        self.load_and_preproc_dataset(fn)
        
    def create_tables(self, src_alphabet, tgt_alphabet):
        if src_alphabet is None:
            self.src_vocab = Dataset.constants + Dataset.hu_alphabet
        else:
            self.src_vocab = Dataset.constants + alphabet
        self.src_table = lookup_ops.index_table_from_tensor(
            tf.constant(self.src_vocab), default_value=Dataset.UNK
        )
        if self.config.share_vocab:
            self.tgt_vocab = self.src_vocab
            self.tgt_table = self.src_table
        else:
            if tgt_alphabet is None:
                self.tgt_vocab = Dataset.constants + Dataset.hu_alphabet
            else:
                self.tgt_vocab = Dataset.constants + alphabet
            self.tgt_table = lookup_ops.index_table_from_tensor(
                tf.constant(self.tgt_vocab), default_value=Dataset.UNK
            )
        self.src_vocab_size = len(self.src_vocab)
        self.tgt_vocab_size = len(self.tgt_vocab)
    
    def load_and_preproc_dataset(self, fn):
        dataset = tf.contrib.data.TextLineDataset(fn)
        dataset = dataset.repeat()
        dataset = dataset.map(lambda s: tf.string_split([s], delimiter='\t').values)
        
        src = dataset.map(lambda s: s[0])
        tgt = dataset.map(lambda s: s[1])
        
        src = src.map(lambda s: tf.string_split([s], delimiter=' ').values)
        src = src.map(lambda s: s[:self.config.src_maxlen])
        tgt = tgt.map(lambda s: tf.string_split([s], delimiter=' ').values)
        tgt = tgt.map(lambda s: s[:self.config.tgt_maxlen])
        
        src = src.map(lambda words: self.src_table.lookup(words))
        tgt = tgt.map(lambda words: self.tgt_table.lookup(words))
        
        dataset = tf.contrib.data.Dataset.zip((src, tgt))
        dataset = dataset.map(
            lambda src, tgt: (
                src,
                tf.concat(([Dataset.SOS], tgt), 0),
                tf.concat((tgt, [Dataset.EOS]), 0),
            )
        )
        dataset = dataset.map(
            lambda src, tgt_in, tgt_out: (src, tgt_in, tgt_out, tf.size(src), tf.size(tgt_in))
        )
        batched = dataset.padded_batch(
            self.config.batch_size,
            padded_shapes=(
                tf.TensorShape([self.config.src_maxlen]),
                tf.TensorShape([self.config.tgt_maxlen+2]),
                tf.TensorShape([None]),
                tf.TensorShape([]),
                tf.TensorShape([]),
            )
        )
        self.batched_iter = batched.make_initializable_iterator()
        s = self.batched_iter.get_next()
        self.src_ids = s[0]
        self.tgt_in_ids = s[1]
        self.tgt_out_ids = s[2]
        self.src_size = s[3]
        self.tgt_size = s[4]
        
    def run_initializers(self, session):
        session.run(tf.tables_initializer())
        session.run(self.batched_iter.initializer)