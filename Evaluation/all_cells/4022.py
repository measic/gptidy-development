sSnsS = sharedSeminormSpanningSystem randomSnorm₀ randomSnorm₁
sSnsS
randomSnorm₀
spanNorm [dv | (dv, Just _)<-sSnsS] :: Seminorm ℝ³
randomSnorm₁
spanNorm $ [dv^*η | (dv, Just η)<-sSnsS]++[dv | (dv, Nothing)<-sSnsS] :: Seminorm ℝ³