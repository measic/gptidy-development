from __future__ import (absolute_import, division, print_function)
from functools import reduce, partial
from operator import mul
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from pyneqsys.symbolic import SymbolicSys, TransformedSys, linear_exprs
sp.init_printing()