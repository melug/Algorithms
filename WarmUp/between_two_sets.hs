

gcd' :: [Int] -> Int
gcd' []     = error "Empty list"
gcd' (x:xs) = foldr gcd x xs

lcm' :: [Int] -> Int
lcm' []     = error "Empty list"
lcm' (x:xs) = foldr lcm x xs

betweenTwoSets :: [Int] -> [Int] -> [Int]
betweenTwoSets a b = let s = lcm' a
                         e = gcd' b 
                      in [ x | x<-[s, s+s .. e], mod e x==0 ]

toInt :: String -> Int
toInt s = read s :: Int

main = do
    line <- getLine
    let (n:m:_) = map toInt $ words line
    line <- getLine
    let a = map toInt $ words line
    line <- getLine
    let b = map toInt $ words line
    putStrLn $ show $ length $ betweenTwoSets a b
