from threading import Thread
from multiprocessing import Process
from timeit import timeit

from fib import fib


def start_jobs(fib_n=10000, n_jobs=10, method=Thread):
    jobs = [method(target=fib, args=(fib_n,)) for _ in range(n_jobs)]
    for job in jobs:
        job.start()
    for job in jobs:
        job.join()


if __name__ == '__main__':
    with open("artifacts/easy.txt", "w") as f:
        f.write(f"threading: {timeit(lambda: start_jobs(method=Thread), number=10)} s.\n")
        f.write(f"multiprocessing: {timeit(lambda: start_jobs(method=Process), number=10)} s.\n")