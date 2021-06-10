def func(a: int, b: int):
    left = a + 1
    right = b - 1
    if left > 5:
        right += 4
    return left * right


res = func(4, 5)
print(res)
