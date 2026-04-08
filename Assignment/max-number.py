list = [1, 5, 4, 2, 3, 9, 7, 8, 6]

max1 = list[0]
max2 = list[0]

for num in list:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2 and num != max1:
        max2 = num

print("Second maximum:", max2)