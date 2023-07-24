config = json.load(open(os.path.expanduser("~/.thesis.conf")))
datasets_path = Path(config['datasets'])
db_folder = Path(config['datasets']) / 'hisdb'
modules   = Path(config['project']) / 'src'

%load_ext autoreload
%autoreload 2
import sys
sys.path.append(str(modules))