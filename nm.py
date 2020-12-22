num = int(input())
nl = [num,0]
m = num

while nl[0] != 0:
    for i in range(len(nl)-nl.count(0)):
        print(nl[i],end=' ')
    if nl[1] == 2:
        nl[1] = 1
        nl.insert(2,1)
    elif nl[0] == 2:
        nl[0] = 1
        nl.insert(2,1)
        m -= 1
    else:
        nl[0] -= 1
        nl[1] += 1
        m -= 1
    print()
