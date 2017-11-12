

-- return (min, max) tuple
min_max :: [Int] -> (Int, Int)
min_max arr = (min0, max0)
    where sum0 = sum arr
          max0 = sum0 - minimum arr
          min0 = sum0 - maximum arr

main = do
    line <- getLine
    let arr = map read (words line) ::[Int]
    let (sum0, sum1) = min_max arr
    putStrLn $ show sum0 ++" "++ show sum1

