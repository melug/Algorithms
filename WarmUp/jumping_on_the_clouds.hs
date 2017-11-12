

cloudCost :: [Int] -> Int -> Int
cloudCost clouds index = (clouds !! index)*2

-- jump until reaches 0th cloud and return left energy
-- k, energy, cloud just reached, clouds
jumpCost :: Int -> Int -> Int -> [Int] -> Int
-- reached 0, return e
jumpCost k e 0 clouds = e-cloudCost clouds 0
jumpCost k e c clouds = jumpCost k (e-1-(cloudCost clouds c)) (mod (c+k) (length clouds)) clouds

jumpCostFrom0 :: Int -> [Int] -> Int
jumpCostFrom0 k clouds = jumpCost k 99 (mod k (length clouds)) clouds

toInt :: String -> Int
toInt s = read s :: Int

main = do
    line1 <- getLine 
    line2 <- getLine 
    let (n:k:_) = map toInt $ words line1
    let clouds = map toInt $ words line2
    putStrLn $ show $ jumpCostFrom0 k clouds
