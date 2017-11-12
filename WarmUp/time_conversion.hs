data TimeReg = AM | PM deriving (Show)
type Time12Hour = (Int, Int, Int, TimeReg)
type Time24Hour = (Int, Int, Int)

split :: [a] -> [Int] -> [[a]]
split arr  []     = [arr]
split []   _      = error "list is empty"
split arr (x:xs)  = let (p0, p1) = splitAt x arr
                     in p0:split p1 xs

toTimeReg :: String -> TimeReg
toTimeReg "AM" = AM
toTimeReg "PM" = PM

decomposeTime12 :: String -> Time12Hour
decomposeTime12 s = let (hour:minute:sec:reg:_) = filter (/=":") $ split s [2, 1, 2, 1, 2]
                   in (read hour::Int, read minute::Int, read sec::Int, toTimeReg reg)

convertFrom12To24 :: Time12Hour -> Time24Hour
convertFrom12To24 (hour, minute, sec, reg) = (newHour, minute, sec)
    where newHour = case reg of 
                      AM -> mod hour 12
                      PM -> if hour<12 then hour+12 else hour

padding :: Int -> String -> String
padding l s = (replicate (max 0 (l-(length s))) '0')++s

intersperse :: a -> [a] -> [a]
intersperse s []     = []
intersperse s [x]    = [x]
intersperse s (x:xs) = x:s:intersperse s xs

show24Hour :: Time24Hour -> String
show24Hour (hour, minute, sec) = concat $ intersperse ":" $ map (padding 2 . show) [hour, minute, sec]

main = do
    clock12 <- getLine
    putStrLn $ show24Hour $ convertFrom12To24 $ decomposeTime12 clock12

