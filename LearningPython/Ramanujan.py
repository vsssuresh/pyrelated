

for hardyTaxi in range(1000, 2000):
    for j in range(1, 20):
        for k in range(1, 20):
            for l in range(1, 20):
                for m in range(1, 20):
                    if ((j * j * j) + (k * k * k) == hardyTaxi and (l * l * l) + (m * m * m) == hardyTaxi) and j != l and k != m and j != m and j < k and l < m and j < l:
                        print(hardyTaxi, j, k, l, m)
	