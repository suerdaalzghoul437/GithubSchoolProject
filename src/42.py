def sum_of_first_n_numbers(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = 5
result = sum_of_first_n_numbers(n)
print(result)  # Output: 15
