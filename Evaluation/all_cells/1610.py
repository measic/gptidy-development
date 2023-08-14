%matplotlib inline

import matplotlib
import matplotlib.pyplot as plt
import gym
import numpy as np
import bisect
import math
import os
import random
import tensorflow as tf

from agents.random_agent import run_episode_random_agent
from agents.human_crafted_agent import human_decision, run_episode_human_crafted_agent

tf.logging.set_verbosity(tf.logging.WARN)  # Remove Info logs