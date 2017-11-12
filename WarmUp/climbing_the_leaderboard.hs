import Data.List (group)

--mergeRank ns ps
mergeRank :: [(Int, Int)] -- list of (number, rank)
          -> [Int]        -- list of number
          -> [Int]        -- lits of ranks for the numbers
mergeRank ns [] = []
mergeRank a@((number, rank):ns) b@(point:ps)
  | point>=number = rank:mergeRank a ps
  | point<number  = mergeRank ns b

numbersWithRank :: [Int]        -- list of numbers
                -> [(Int, Int)] -- list of (number, rank)
numbersWithRank arr = let grouped_arr = group arr
                       in zipWith combine grouped_arr [1..]
    where combine (x:xs) i = (x, i)

main = do
    n_temp <- getLine
    let n = read n_temp :: Int
    scores_temp <- getLine
    let scores = map read $ words scores_temp :: [Int]
    m_temp <- getLine
    let m = read m_temp :: Int
    alice_temp <- getLine
    let alice = map read $ words alice_temp :: [Int]
    let new_alice = reverse alice
    let new_scores = scores ++ [(minimum alice)]
    putStrLn $ unlines $ map show $ reverse $ mergeRank (numbersWithRank new_scores) new_alice
