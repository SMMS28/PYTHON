fnum = int(input("Enter Your First Num: "))
opt = {"+","-","*","/"}
for i in opt:
    print(i)
op = input("Pick an operation")
lnum = int(input("Enter Your Last Num: "))

def calc(first,last):
    """Calculates the both nums based on the selected operation
        Usage:
        calc(first,last) => (num,num)    
    """
    if op == "+":
        return f"{first} + {last} = {first + last}"
    elif op == "-":
        return f"{first} - {last} = {first - last}"
    elif op == "*":
        return f"{first} * {last} = {first * last}"
    elif op == "/":
        return f"{first} / {last} = {first / last}"
    else:
        return "Invalid option"
print(calc(first=fnum,last=lnum))