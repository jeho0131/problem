rcp = [0 for i in range(3)]
num = int(input())
win = 0

for i in range(0, num+1):
    for j in range(0, num-i+1):
        rcp[0] = i
        rcp[1] = j
        rcp[2] = num-i-j

        if rcp.count(max(rcp)) == 1:
            win += 1
print(win)
