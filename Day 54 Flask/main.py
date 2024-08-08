import time


# print(current_time)  # seconds since Jan 1st, 1970


# Write your code below 👇

def speed_calc_decorator(function):
    def inner():
        current_time = time.time()
        function()
        time_diff = time.time() - current_time
        print(time_diff)

    return inner


@speed_calc_decorator
def fast_function():
    for i in range(1000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(10000000):
        i * i


slow_function()
