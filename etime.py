sm = [6,2,5,5,4,5,6,3,7,6]
t = int(input())

hms = [[0 for i in range(2)]for i in range(3)]
add = 0
time = 0

for i in range(0,24):
    for j in range(0,60):
        for k in range(0,60):
            hms[0][0] = int(i/10)
            hms[0][1] = i % 10
            hms[1][0] = int(j/10)
            hms[1][1] = j % 10
            hms[2][0] = int(k/10)
            hms[2][1] = k % 10
            for a in range(3):
                add += sm[hms[a][0]]
                add += sm[hms[a][1]]
            if add == t:
                time += 1
            add = 0
            
print(time)
