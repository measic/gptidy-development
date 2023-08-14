Norm nev₀ = spanNorm [ex.⊗(1.0,0.0) ^+^ ey.⊗(0.0,0.0),ex.⊗(0.0,1.0) ^+^ ey.⊗(-1.0,0.0)] :: Norm (ℝ²+>(ℝ,ℝ))
Norm nev₁ = Norm uncanonicallyToDual :: Norm (ℝ²+>(ℝ,ℝ))
nevs = arr $ nev₀^+^nev₁ :: (ℝ²+>(ℝ,ℝ))+>(ℝ²⊗(ℝ,ℝ))
δj = LinearMap $ V2 (0,1) (0,0) :: ℝ²+>(ℝ,ℝ)