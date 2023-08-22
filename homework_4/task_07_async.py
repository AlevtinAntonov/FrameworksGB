import asyncio
import time
from random import randint

res = 0


async def sum_list(lst):
    global res
    for i in lst:
        res += i


async def main(sep_list):
    tasks = []

    for sep in sep_list:
        aio_task = asyncio.ensure_future(sum_list(sep))
        tasks.append(aio_task)
    await asyncio.gather(*tasks)


def task(lst=None):
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main(lst))

    return res, time.time() - start_time


if __name__ == "__main__":
    lst = [randint(1, 100) for _ in range(1_000_000)]
    sep_list = [lst[i:i + 100_000] for i in range(0, 1_000_000, 100_000)]

    result = task(sep_list)
    print(f'Результат асинхронного расчёта: {result[0]} за {result[1]:.2f} секунд')