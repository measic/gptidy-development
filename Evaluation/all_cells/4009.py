rough = roughEigenSystem euclideanNorm h
forM_ (take 3 $ iterate (finishEigenSystem euclideanNorm) rough) $ \vs -> do
   forM_ vs $ \ev -> putStrLn $ "λ = " ++ showGFloat (Just 5) (ev_Eigenvalue ev)
                                ",\t±" ++ showGFloat (Just 1) (ev_Badness ev)
                                "\t: " ++ show (ev_Eigenvector ev)
   putStrLn ""