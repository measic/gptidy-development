esyss = constructEigenSystem euclideanNorm 1e-8 (arr h) [V3 1 2 3]

import Numeric (showGFloat)

forM_ (take 12 esyss) $ \vs -> do
   forM_ vs $ \ev -> putStrLn $ "λ = " ++ showGFloat (Just 5) (ev_Eigenvalue ev)
                                ",\t±" ++ showGFloat (Just 1) (ev_Badness ev)
                                "\t: " ++ show (ev_Eigenvector ev)
   putStrLn ""