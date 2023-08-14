shSys = sharedNormSpanningSystem (spanNorm [V2 1 0, V2 0 1]) (spanNorm [V2 1 0, V2 0 2] :: Norm ℝ²)
spanNorm $ fst<$>shSys           :: Norm ℝ²
spanNorm [η*^dv | (dv,η)<-shSys] :: Norm ℝ²