import itertools

def graduation(n):

    lst = [list(i) for i in itertools.product([0, 1], repeat=n)]

    k=0
    l = []
    z=[]

    for i in lst:
        j = 0
        while j+3 < n:
            try:
                if i[j] == 0 and i[j+1] == 0 and i[j+2] == 0 and i[j+3] == 0:
                    k+=1
                    l.append(i)
                    break
            except:
                pass
            j+=1

    d = len(lst)-k
    y=[]
    for x in lst:
        if x in l:
            pass
        else:
            if x[-1] == 0:
                y.append(x)

    print(str(len(y))+'/'+str(d))

file1 = open('impact_assignment.txt', 'r')
Lines = file1.readlines()

for line in Lines:
    graduation(int(line.strip()))
    # print("{}".format(line.strip()))
