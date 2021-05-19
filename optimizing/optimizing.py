from functools import lru_cache
import time

def profiler(func):
    def wrapper(*args, **kwargs):
        # start = time.perf_counter()  # Alternatively, you can use time.process_time()
        start = time.process_time()
        func_return_val = func(*args, **kwargs)
        # end = time.perf_counter()
        end = time.process_time()
        print('{0:<10}.{1:<8} : {2:<8}'.format(func.__module__, func.__name__, end - start))
        return func_return_val
    return wrapper

@profiler
def fib(x):
    """ Prints the fibonacci series up to the x'th fibonacci number"""
    if x <= 1:
        return x
    else:
        fib_arr = [0, 1]
        s = "0, 1"
        for i in range(2, x):
            fib_arr.append(fib_arr[i-1] + fib_arr[i - 2])
            s += ', ' + str(fib_arr[i-1] + fib_arr[i - 2])
    print(s)
    return fib_arr[-1]

@profiler
@lru_cache(maxsize=12)
def fib_fast(x):
    """ Prints the fibonacci series up to the x'th fibonacci number"""
    if x <= 1:
        return x
    else:
        fib_arr = [0, 1]
        s = "0, 1"
        for i in range(2, x):
            fib_arr.append(fib_arr[i-1] + fib_arr[i - 2])
    print(', '.join(map(str,fib_arr)))
    ''.join(map(str,fib_arr))
    return fib_arr[-1]

if __name__ == "__main__":
    print('{0:<10} {1:<8} {2:^8}'.format('module', 'function', 'time'))
    x = 5
    fib(x) # 0, 1, 1, 2, 3
    x = 20
    fib(x)
    x = 100
    fib(x)

    x = 5
    fib_fast(x)
    x = 20
    fib_fast(x)
    x = 100
    fib_fast(x)
