randomSnorm₀ = spanNorm [V3 (-5.0406) 6.7142 (-6.1288), V3 9.2645 3.3900 (-7.3202)] :: Seminorm ℝ³
randomSnorm₁ = spanNorm [V3   4.5582  2.7252 (-5.9800), V3 (-4.8086) 2.15705 3.2654] :: Seminorm ℝ³
sNsS = sharedNormSpanningSystem randomSnorm₀ randomSnorm₁
sNsS
randomSnorm₀
spanNorm (fst <$> sNsS) :: Seminorm ℝ³