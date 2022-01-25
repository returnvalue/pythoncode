import memory_profiler as mem_profile
import random
import time

mem_before = mem_profile.memory_usage()[0]
print(f'Before calling the function, Python is using {mem_before} MB of memory')


def cubed_list(n):
    result = []
    for i in range(n):
        result.append(i ** 3)
    return result


def cubed_generator(n):
    for i in range(n):
        yield i ** 3


time_start = time.perf_counter()
cubes = cubed_generator(5000000)
time_end = time.perf_counter()
elapsed = time_end + time_start

mem_after = mem_profile.memory_usage()[0]
mem_usage = mem_after - mem_before

print(f'After calling the function, Python is using {mem_after} MB of memory')
print(f'It Took {elapsed} Seconds to cube 5,000,000 integers')