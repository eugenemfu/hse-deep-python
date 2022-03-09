import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from timeit import timeit
import os


def count_and_log(args):
    with open('artifacts/medium_log.txt', 'a') as file:
        file.write(f'Calculating f({args[1]})\n')
    return args[0](args[1])


def integrate(f, a, b, method=ThreadPoolExecutor, n_jobs=1, n_iter=500):
    step = (b - a) / n_iter
    args = [(f, a + i * step) for i in range(n_iter)]
    with method(max_workers=n_jobs) as t:
        return step * sum(t.map(count_and_log, args))


if __name__ == "__main__":
    with open('artifacts/medium_log.txt', 'w') as file:
        file.write('')

    n_jobs_list = list(range(1, 2 * os.cpu_count() + 1))
    thread_times = []
    process_times = []
    for n_jobs in n_jobs_list:
        time = timeit(lambda: integrate(math.cos, 0, math.pi / 2, ThreadPoolExecutor, n_jobs), number=1)
        thread_times.append(time)
        time = timeit(lambda: integrate(math.cos, 0, math.pi / 2, ProcessPoolExecutor, n_jobs), number=1)
        process_times.append(time)

    with open("artifacts/medium_times.txt", "w") as f:
        f.write(f'n_jobs: {n_jobs_list}\n')
        f.write(f'thread: {thread_times}\n')
        f.write(f'process: {process_times}\n')