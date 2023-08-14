spannableNorm :: Norm (ℝ,ℝ)
spannableNorm = Norm (LinearFunction $ \(x,y) ->
                       x*^(0.17378081543539758,-0.4560331366132637)
                   ^+^ y*^(-0.4560331366132637,1.8015855966507703) )
normSpanningSystem' spannableNorm
dualBasisCandidates [(0,(2.398827862960816,0.0)),(1,(3.3741436411530183,1.2857869007290879) :: (ℝ,ℝ))]
spannableNorm