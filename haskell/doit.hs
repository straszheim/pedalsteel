-- import Prelude hiding ((++))

data Letternote = C | Cs | D | Ds | E | F | Fs | G | Gs | A | As | B 
                  deriving (Show, Enum)

data Interval = U1 | Min2 | Maj2 | Min3 | Maj3 | P4 | Dim4 | 
                P5 | Min6 | Maj6 | Min7 | Maj7 | P8
                deriving (Show, Enum)

data Chord = Chord [Interval]
             deriving (Show)

--data Changes = P1 | P2 | P3 | P4 | P5 | P6 | P7 | P8 | 
--               LL | LU | LR | RL | RR
--               deriving (Show)

data Neck = Neck { tuning :: [Letternote] }

min7 = [U1, Min3, P5, Min7]
maj7 = [U1, Maj3, P5, Maj7]

class Noteable n where
      (<<) :: n -> n -> Bool
      (+.)  :: n -> n -> [n]
      plus :: n -> Interval -> n
      (.+) :: n -> Interval -> n

instance Noteable Letternote where
         x << y = fromEnum x < fromEnum y
         x +. y = [x, y]
         plus x y = toEnum ((fromEnum x) Prelude.+ (fromEnum y) `mod` 12)::Letternote
         x .+ y = plus x y

--instance Num Letternote where
--         x + y = toEnum (((fromEnum x) + y) `mod` 12)::Letternote


cmaj7 = map (plus C) maj7
cmin7 = map (plus C) min7

sth = C .+ Maj3
-- main = putStrLn $ show 

                     