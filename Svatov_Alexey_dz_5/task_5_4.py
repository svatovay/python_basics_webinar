src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 98]
result = [num for i, num in enumerate(src) if src[i - 1] < num and i > 0]
print(result)
