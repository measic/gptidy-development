movies_tp = movies.T
moviesnormal = (movies_tp - movies_tp.min()) / (movies_tp.max() - movies_tp.min())
moviesnormal