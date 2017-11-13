

insert :: Int -> [Int] -> [Int]
insert x []     = [x]
insert x (y:ys) 
  | x<y       = x:y:ys
  | otherwise = y:insert x ys

insertion_sort :: [Int] -> [Int]
insertion_sort [] = []
insertion_sort (x:xs) = insert x $ insertion_sort xs
