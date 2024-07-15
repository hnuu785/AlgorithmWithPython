N, M = map(int, input().split())

arr = []
tmp = []

for t1 in range(N):
    arr.append(t1 + 1)
    tmp.append(arr[t1])

for t1 in range(M):
    for t2 in range(N):
        tmp[t2] = arr[t2]
    i, j = map(int, input().split())
    t3 = 0
    for t2 in range(i, j + 1):
        arr[t2 - 1] = tmp[j - 1 - t3]
        t3 += 1

for t1 in range(N):
    print(f"{arr[t1]}", end=" ")