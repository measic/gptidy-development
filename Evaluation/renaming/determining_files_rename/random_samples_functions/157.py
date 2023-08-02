class Config(object):
    default_fn = os.path.join(PROJECT_DIR, 'config', 'seq2seq', 'default.yaml')

    @staticmethod
    def function_def(fn=default_fn):
        with open(fn) as f:
            return yaml.load(f)

    @classmethod
    def from_yaml(cls, fn):
        params = yaml.load(fn)
        return cls(**params)

    def __init__(self, **kwargs):
        defaults = Config.load_defaults()
        for param, val in defaults.items():
            setattr(self, param, val)
        for param, val in kwargs.items():
            setattr(self, param, val)
config = Config(src_maxlen=30, tgt_maxlen=33)
dataset = Dataset(input_fn, config)