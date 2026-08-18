def decToBin(num:int)->int:
    binary=''
    while num>=2:
        if not(num/2).is_integer():
            binary+="1"
            num//=2
        else:
            binary+="0"  
            num//=2

    binary+="1"
    binary=binary[::-1]
    binary=int(binary)
    return binary


print(decToBin(0))




            

