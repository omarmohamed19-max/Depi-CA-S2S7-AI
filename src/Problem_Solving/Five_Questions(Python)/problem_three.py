def Prime_Factors(num:int)->list:
    factor=[]
    divisor=2

    while divisor*divisor<=num:
        while num%divisor==0:
            factor.append(divisor)
            num//=divisor
        divisor+=1

    if num>1:
        factor.append(num)    

    return factor             

print(Prime_Factors(56))
