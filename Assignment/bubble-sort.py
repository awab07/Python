s = [6, 7, 9, 1, 2, 3, 4, 5, 8]

n = len(s)
for i in range(n):
    for j in range(0, n - i - 1):
        if s[j] < s[j + 1]:  
            s[j], s[j + 1] = s[j + 1], s[j]
print(s)