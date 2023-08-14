Just (Lens emb) = embedFreeSubspace [V2 1 1, V2 2 0 :: V2 ℝ]
V2 4 0 & emb %~ map (^2)