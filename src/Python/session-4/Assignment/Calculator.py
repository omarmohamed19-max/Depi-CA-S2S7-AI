
# name : omar mohamed fathy

print('''
Welcome to the Simple Calculator! 
Select an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
''')

while True:



    operation=input("Enter your choice (1/2/3/4) or 'exit' to quit : ")
    if operation=="1" or operation=="2" or operation=="3" or operation=="4" or operation.lower()=="exit":
        if operation.lower()=="exit":
            break
        while True:
            try:
                one=float(input("Enter First Number : "))
                two=float(input("Enter Second Number : "))
                break
            except Exception as e:
                print(f"Invalid Value, please try again")
        
        if operation=="1":
            print(f"{one} + {two} = {one+two}")
        elif operation=="2":
            print(f"{one} - {two} = {one-two}")
        elif operation=="3":
            print(f"{one} * {two} = {one*two}")
        elif operation=="4":
            while two==0:
                print("division by zero not allowed , try again")
                two=float(input("Enter Second Number : "))
                
            print(f"{one} / {two} = {one/two}")
        
    else:
        print("Invalid Choice ,try again\n")    

print("Exiting the Calculator. Goodbye!")    

