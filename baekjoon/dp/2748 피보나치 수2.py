# ~ 10분
n = int(input())

d = [0] * 1000
d[0] = 0
d[1] = 1
# d = [0, 1]

for i in range(2, n+1):
    d[i] = d[i-1] + d[i-2]
    # d.append(d[i-1] + d[i-2])

print(d[n])
