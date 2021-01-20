n  = int(input())
l = [[] for i in range(n)]
xx = n-1
pm = -1
p = 1

for y in range(n):
    for x in range(n):
        l[xx+x*pm].append(p)
        p += 1
    xx += x*pm
    pm = pm * -1

for pl in range(n):
    for ppl in range(n):
        print(l[pl][ppl], end=" ")
    print()
