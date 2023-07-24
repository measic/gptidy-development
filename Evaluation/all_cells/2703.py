import pandas as pd
import numpy as np
import os
try:
    import arcpy
except ImportError:
    pass

OVERWRITE = True
PATH = os.path.join('.', 'data')

# TODO: There's some data that is inclued as a sort of separate table with the .xlsx file, that we are just throwing away at present
# TODO: Handle combined precincts
# TODO: Delete superfluous fields from derived_data.gdb/blocks