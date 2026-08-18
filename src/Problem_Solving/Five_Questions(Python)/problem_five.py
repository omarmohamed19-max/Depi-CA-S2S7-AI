def PerfectNums(n1:int,n2:int)->int:
    count=0
    perfect_list=[]
    for i in range(max(n1,1),n2+1):
        for j in range(1,i):
            if i%j==0:
                count+=j
        if i==count:
            perfect_list.append(i)
        count=0

    return perfect_list

print(PerfectNums(0,555))        


