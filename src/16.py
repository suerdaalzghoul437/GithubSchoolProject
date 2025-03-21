def sum_of_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6

for i in range(100):
    print(sum_of_squares(i))
