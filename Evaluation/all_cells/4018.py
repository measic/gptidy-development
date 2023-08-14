Norm obliqueN = spanNorm [(0.4168702621144828,-1.0939449945413133),(0.0,0.777733852657049)] :: Norm (ℝ,ℝ)
arr obliqueN <$> [(1,0),(0,1)]
arr (pseudoInverse $ arr obliqueN) <$> [(1,0),(0,1)]