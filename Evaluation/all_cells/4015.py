inj :: ℝ² +> ℝ³
inj =  ex.<V2 1 0
   ^+^ ey.<V2 2 1
   ^+^ ez.<V2 2 3
inj' = pseudoInverse inj
inj . inj'
inj' . inj