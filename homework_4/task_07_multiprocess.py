from multiprocessing import Pool
import time
from random import randint


def sum_list(lst):
    res = 0
    for i in lst:
        res += i

    return res


def task(sep_list):
    start_time = time.time()

    pool = Pool(processes=10)
    result = pool.map(sum_list, sep_list)

    return sum(result), time.time() - start_time


if __name__ == "__main__":
    lst = [randint(1, 100) for _ in range(1_000_000)]
    sep_list = [lst[i:i + 100_000] for i in range(0, 1_000_000, 100_000)]

    result = task(sep_list)
    print(f'Результат многопроцессорного расчёта: {result[0]} за {result[1]:.2f} секунд')
