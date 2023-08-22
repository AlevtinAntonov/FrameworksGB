import threading
import time
from random import randint

res = 0


def sum_list(lst):
    global res
    for i in lst:
        res += i


def task(sep_list):
    threads = []
    start_time = time.time()

    for sep in sep_list:
        thread = threading.Thread(target=sum_list, args=[sep])
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return res, time.time() - start_time


if __name__ == "__main__":
    lst = [randint(1, 100) for _ in range(1_000_000)]
    sep_list = [lst[i:i + 100_000] for i in range(0, 1_000_000, 100_000)]

    result = task(sep_list)
    print(f'Результат многопоточного расчёта: {result[0]} за {result[1]:.2f} секунд')
