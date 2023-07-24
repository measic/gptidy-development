import os
from datetime import datetime

filepath = datetime.now().strftime('logs/%Y/%m/%d') + '/' + 'hello.txt'
# filepath = 'dir1/dir2/dir3/hello.txt'

dirpath = os.path.dirname(filepath)  # 'dir1/dir2/dir3'
if not os.path.exists(dirpath):
    os.makedirs(dirpath)

f = open(filepath, 'wt', encoding='utf8')
f.write('가나다')
f.close()