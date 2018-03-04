--f :: [Int] -> [Int]
--f n arr = [ a | a <- arr, i <- [1..n]]
--f n arr = [a | a <- arr, n > a]
--f [] = []
--f lst = [v | (v,i) <- zip lst [0..], odd i]

--f arr = sum [ n | n <- arr, odd n ]

--solve :: Double -> Double
--solve x = 1 + sum [ product [x | i <- [1..j] ] / product [1..j] | j <- [1..9]]

solve :: Int -> Int -> [Int] -> [Int] -> [Double]
solve l r a b = 
    do
        let abzip = zip a b
        let xr = [l,l + 0.001..r]
        let fx = [sum [fromIntegral fst ab * fromIntegral x ^ fromIntegral snd ab | ab <- abzip] :: Double | x <- xr]::[Double]
        let area = sum [ f * 0.001 | f <- fx ]
        let vol = sum [ pi * r * r * 0.001| r <- fx ]
        return [area, vol]::[Double]

