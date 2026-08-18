def is_prime(num:int)->bool:
    if num<2:
        return False
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            return False
    return True

print("Twin Prime :")
for i in range(3,1000):
    if is_prime(i)and is_prime(i+2):
        print(f"{i} and {i+2}")

