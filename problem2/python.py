# Answer1

def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 2
    else:
        return fib(n-1) + fib(n-2)

i = 0
result = 0
while True:
    next = fib(i)
    if next > 4000000:
        break
    elif next % 2 == 0:
        result += next
    i += 1
print(result)
