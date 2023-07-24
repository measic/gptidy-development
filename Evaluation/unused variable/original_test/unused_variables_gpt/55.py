# Common imports
import numpy as np
import matplotlib.pyplot as plt
import os

# setting random seed
np.random.seed(42)


# To plot pretty figures
%matplotlib inline
import matplotlib
plt.rcParams['axes.labelsize'] = 14
plt.rcParams['xtick.labelsize'] = 12
plt.rcParams['ytick.labelsize'] = 12


CHAPTER_ID = "ensembles"

def image_path(fig_id):
    
    if os.path.exists(os.path.join("images", CHAPTER_ID)):
        return os.path.join("images", CHAPTER_ID, fig_id)
    os.mkdir(os.path.join("images", CHAPTER_ID))
    return os.path.join("images", CHAPTER_ID, fig_id)

def save_fig(fig_id, tight_layout=True):
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(image_path(fig_id) + ".png", format='png', dpi=300)