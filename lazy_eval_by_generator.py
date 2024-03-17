
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib_seq = fibonacci()

for _ in range(4):
    print(next(fib_seq))
  
