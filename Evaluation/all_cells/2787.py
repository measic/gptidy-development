import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import warnings

from pybbn.generator.bbngenerator import generate_singly_bbn, generate_multi_bbn, convert_for_exact_inference
from pybbn.generator.bbngenerator import convert_for_drawing
from pybbn.pptc.inferencecontroller import InferenceController

np.random.seed(37)

g, p = generate_multi_bbn(5, max_iter=5)
m_bbn = convert_for_exact_inference(g, p)
nx_multi_bbn = convert_for_drawing(m_bbn)

g, p = generate_singly_bbn(5, max_iter=10)
s_bbn = convert_for_exact_inference(g, p)
nx_singly_bbn = convert_for_drawing(s_bbn)