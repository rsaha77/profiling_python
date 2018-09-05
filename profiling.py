# https://www.youtube.com/watch?v=8qEnExGLZfY (Good explanation of cProfile)
# https://zapier.com/engineering/profiling-python-boss/ (The method do_cprofile is taken from here)

import cProfile

def do_cprofile(func):
    def profiled_func(*args, **kwargs):
        profile = cProfile.Profile()
        try:
            profile.enable()
            result = func(*args, **kwargs)
            profile.disable()
            return result
        finally:
            profile.print_stats()
    return profiled_func


def fibonacci(max_num, a=1, b=1):
    if a > max_num:
        print(b - a)
        return
    else:
        fibonacci(max_num, b, a+b)


def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def mul(x, i):
    return x * i


def f(x, num):
    for i in range(1, num + 1):
        x = mul(x,i)
    return x


@do_cprofile
def factorial_loop(num):
    x = 1
    print(f(x, num))


# fibonacci(10000000000)
# print(factorial(10))
factorial_loop(10000)

