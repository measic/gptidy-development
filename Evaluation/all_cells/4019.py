spannableNorm :: Norm ℝ²
spannableNorm = Norm (LinearFunction $ \(V2 x y) ->
                       x*^(V2 0.17378081543539758 (-0.4560331366132637))
                   ^+^ y*^(V2 (-0.4560331366132637) 1.8015855966507703) )
normSpanningSystem' spannableNorm
dualBasisCandidates [(0,(V2 2.398827862960816 0.0)),(1,(V2 3.3741436411530183 1.2857869007290879) :: ℝ²)]
spannableNorm