def rv(l):
    ll = [0 for i in range(9)]
    for i in range(0,5):
        ll = l[0:l[0]]
        ll.reverse()
        for i in range(l[0]):
            l[i] = ll[i]
        if l[0] == 1:
            return 1
    return 0

#def ml(l,n,ll):

l = [2,3,4,5,6,7,8,9,1]
print(rv(l))
