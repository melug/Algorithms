

toInt :: String -> Int
toInt s = read s :: Int

maximum_diff :: Int -> [Int] -> Int
maximum_diff k numbers = max (maximum numbers - k) 0

main = do
    line <- getLine
    let (n:k:_) = map toInt $ words line
    line <- getLine
    let hurdles = map toInt $ words line
    print $ maximum_diff k hurdles
