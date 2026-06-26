# Задание 5

diqits = [1,2,3]

def plusOne(diqits):
    n = len(diqits)

    for i in range(n-1,-1,-1):
        if diqits[i] < 9:
            diqits[i] += 1
            return diqits
        else:
            diqits[i] = 0

            