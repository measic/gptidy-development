# For your convenience, you can run this cell to run all the tests at once!
import glob
from gofer.ok import check_all
display(check_all(glob.glob('tests/q*.py')))