class Clustering:
    """Base class of clustering, offering basic and common variables and operations for clustering."""

    data: Any  # array-like (List, pd.Series, np.ndarray((N, L))) data
    names: List[str] = None  # of each data; displayed in plots
    N: int = field(init=False)  # number of data; = len(data) or data.shape[0]
    L: int = field(init=False, default=None)  # number of features; = data.shape[1]
    assignments: np.ndarray = field(init=False)  # cluster assignment for each data; int type of length N
    s_dist_mat: np.ndarray = field(init=False, default=None)  # square distance matrix
    c_dist_mat: np.ndarray = field(init=False, default=None)  # condensed distance matrix
    cache: dict = field(default_factory=dict)  # store large intermediate data