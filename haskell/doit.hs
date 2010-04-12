
f x = x * 4

x = [1,2,3]

class (Enum n) => Noteable n where
      (<<) :: n -> n -> bool
      (++)  :: n -> n -> [n]
      --      x << y = fromenum x < fromenum y

data Letternote = c | cs | d | ds | e | f | fs | g | gs | a | as | b 
                  deriving (show, enum)

instance Noteable Letternote where
         x << y = fromEnum x < fromEnum y
         x ++ y = [x, y]

data Interval = U1 | Min2 | Maj2 | Min3 | Maj3 | P4 | Dim4 
                | P5 | Min6 | Maj6 | Min7 | Maj7 | P8
                deriving (Show, Enum)

min7Chord = [U1, Min3, P5, Min7]


addy n i = toEnum ((fromEnum n) + (fromEnum i) `mod` 12)::Letternote

dawg = "hi"

doit = addy C Maj3

main = do
     putStrLn "hi"
