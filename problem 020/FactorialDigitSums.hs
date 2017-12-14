solve :: Integer -> Integer
solve x = fold(split(show (factorial x) :: String))
    
split :: [Char] -> [Integer]
split []        = []
split (x:xs)    = [read [x] :: Integer] ++ split xs

fold :: [Integer] -> Integer
fold []         = 0
fold (x:xs)     = x + fold(xs)

factorial :: Integer -> Integer
factorial n = product [1..n]

main = do
    solve <- getContents    
    print $ solve
