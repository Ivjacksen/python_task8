import time
import psutil
import os

# Декоратор, замеряющий время выполнение декорируемой функции
def time_func(func):
    def wapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f'Время выполнения декорируемой функции: {end_time-start_time} сек.')
        return result
    return wapper

# Декоратор, замеряющий объем использования памяти.
def memory_func(func):
    def wapper(*args, **kwargs):
        proc = psutil.Process(os.getpid())
        start_memory = proc.memory_info().rss
        result = func(*args, **kwargs)
        end_memory = proc.memory_info().rss
        print(f"Объем памяти используемой функцией: {end_memory-start_memory} байт")
        return result
    return wapper


@memory_func
@time_func
def gen_list_nat(num):
    for i in range(num):
        yield i


@memory_func
@time_func
def list_nat(num):
    result = []
    for i in range(num):
        result.append(i)
    return result


gen_list_nat(10000000)
list_nat(10000000)