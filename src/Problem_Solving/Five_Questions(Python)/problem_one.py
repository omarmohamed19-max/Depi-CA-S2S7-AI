def multiplication(num:int):
    for i in range(1,11):
        print(f"{num} * {i} = {num*i}")

try:
    number=float(input("Enter your Number : "))
    multiplication(number)
except Exception as e:
    print(f"Invalid value")    