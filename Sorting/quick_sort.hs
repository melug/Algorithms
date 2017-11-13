

quick_sort :: [Int] -> [Int]
quick_sort []  = []
quick_sort [x] = [x]
quick_sort (a:arr) = quick_sort lower ++ [a] ++ quick_sort greater
    where lower   = filter (<a) arr
          greater = filter (>=a) arr
