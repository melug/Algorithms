import Data.List (sort)

toInt :: String -> Int
toInt s = read s :: Int

readInts :: IO [Int]
readInts = do
    line <- getLine
    return $ map toInt $ words line

readTL :: Int -> IO [(Int, Int)]
readTL 0 = do return []
readTL n = do
    (t:l:_) <- readInts
    rest <- readTL (n-1)
    return $ (t,l): rest

splitWithPredicate :: (a -> Bool) -> [a] -> ([a], [a])
splitWithPredicate f xs = (filter f xs, filter (not . f) xs)

main = do
    (n:k:_) <- readInts
    tls <- readTL n
    let (is, us) = splitWithPredicate (\(a, b) -> b==1) tls
    let it = sum $ map (\(a, b) -> a) is
    let ut = sum $ map (\(a, b) -> a) us
    let it = it - :
    print $ it + ut

