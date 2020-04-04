def f(raw_arr):
    a = []
    for i in range(len(raw_arr)):
        a.append((raw_arr[i][0], raw_arr[i][1], i))
    a.sort()
    c_end = 0
    j_end = 0
    result = []
    for start, end, i in a:
        if start < c_end and start < j_end:
            return "IMPOSSIBLE"
        if start >= c_end:
            result.append(('C', i))
            c_end = end
        else:
            result.append(('J', i))
            j_end = end
    res = ''
    for c, i in sorted(result, key=lambda x: x[1]):
        res += c
    return res
T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = []
    for _ in range(N):
        interval = [int(s) for s in input().split(" ")]
        arr.append(interval)
    res = f(arr)
    print("Case #{}: {}".format(t, res))