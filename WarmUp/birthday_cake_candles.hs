

-- return (min, max) tuple
highest_numbers :: [Int] -> [Int]
highest_numbers arr = filter (==highest_number) arr
    where highest_number = maximum arr

main = do
    number_of_candles <- getLine
    candles_str <- getLine
    let numbers = map read (words candles_str) :: [Int]
    putStrLn $ (show . length . highest_numbers) numbers

