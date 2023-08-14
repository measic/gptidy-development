quadratMat :: ℝ⁴ +> (ℝ² +> ℝ²)
quadratMat = arr.LinearFunction $ \(V4 a b c d)
          -> arr.LinearFunction $ \(V2 x y) -> V2 (a*x + b*y) (c*x + d*y)
second ($[]) $ decomposeLinMap quadratMat
flattenQuadrat :: (ℝ²⊗ℝ²) +> ℝ⁴
flattenQuadrat = adjoint $ quadratMat
second ($[]) $ decomposeLinMap flattenQuadrat
flattenQuadrat \$ V4 1 2 3 4