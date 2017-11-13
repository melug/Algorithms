import Data.List (sort)

merge :: [Int] -> [Int] -> [Int]
merge [] arr1 = arr1
merge arr0 [] = arr0
merge ax@(x:xs) ay@(y:ys)
  | x < y     = x:merge xs ay
  | otherwise = y:merge ys ax

divide :: [Int] -> ([Int], [Int])
divide arr = splitAt mid arr
    where mid = div (length arr) 2

merge_sort :: [Int] -> [Int]
merge_sort []  = []
merge_sort [x] = [x]
merge_sort arr = merge (merge_sort arr0) (merge_sort arr1)
    where (arr0, arr1) = divide arr

prop_merge_sort :: [Int] -> Bool
prop_merge_sort arr = merge_sort arr == sort arr
