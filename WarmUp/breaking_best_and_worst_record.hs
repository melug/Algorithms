
accumulate :: (Int, Int, Int, Int)  -- best, worst scores and number of breaks respectively
           -> Int                   -- new score
           -> (Int, Int, Int, Int)  -- new accumulator value
accumulate (bscore, wscore, nbs, nws) score
  | score > bscore = (score, wscore, nbs+1, nws)
  | score < wscore = (bscore, score, nbs, nws+1)
  | otherwise      = (bscore, wscore, nbs, nws)

countRecords :: [Int] -> (Int, Int, Int, Int)
countRecords (s:ss) = foldl accumulate (s, s, 0, 0) ss

toInt :: String -> Int
toInt s = read s :: Int

main = do
    line <- getLine
    let n = toInt line
    line <- getLine
    let (_, _, nbs, nws) = countRecords $ map toInt $ words line
    putStrLn $ unwords $ map show [nbs, nws]
