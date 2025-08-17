def print_fibonacci(length):
    if length <= 0:
        print([])
        return
    
    if length == 1:
        print([0])
        return
    
    fib = [0, 1]
    while len(fib) < length:
        fib.append(fib[-1] + fib[-2])
    
    print(fib)

