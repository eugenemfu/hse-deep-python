def fib(n):
    ans = [0, 1]
    for _ in range(n - 1):
        ans.append(ans[-1] + ans[-2])
    return ans[-1]
