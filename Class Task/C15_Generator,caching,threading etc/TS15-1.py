def fibonacci_num(max_number):
    yield 0
    yield 1
    num1 = 0
    num2 = 1
    cur = 0;
    while (num1 + num2 ) <= max_number:
        cur = num1 + num2
        yield cur
        num1 = num2
        num2 = cur

x = fibonacci_num(40)

print(next(x))
print(next(x))
print(next(x))
# for p in x:
#     print(p)