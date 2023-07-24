{-# LANGUAGE TypeOperators #-}

import Math.LinearMap.Category
import Data.VectorSpace
import Data.VectorSpace.Free
import Linear (V2(..), V3(..), V4(..), ex, ey, ez)
import Control.Category.Constrained.Prelude
import Control.Arrow.Constrained
import Prelude ()
import Control.Lens hiding ((<.>))

:opt no-lint