def add(x, y): return x + y
def sub(x, y): return x - y
def mul(x, y): return x * y
def div(x, y): return x / y

# PEP 8:E731
# Always use a def statement instead of an assignment statement that binds a lambda expression directly to a name.
# add = lambda x,y: x + y
# sub = lambda x,y: x - y
# mul = lambda x,y: x * y
# div = lambda x,y: x / y


calculator = """
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
"""

current_total = 0

print(calculator)
print("A simple calculator.")
print("+\n-\n*\n/")

num1 = float(input("What's your first number? "))

calculating = True
while calculating:

    oper = input("Pick an operation: ")
    num2 = float(input("What's the next number? "))

    if oper == '+':
        current_total = add(num1, num2)
    elif oper == '-':
        current_total = sub(num1, num2)
    elif oper == '*':
        current_total = mul(num1, num2)
    elif oper == '/':
        current_total = div(num1, num2)

    print(f"{num1} {oper} {num2} = {current_total}")

    calc_current = input(f"Type 'y' to continue calculating with {current_total}, "
                         f"or type 'n' to start a new calculation: ")

    if calc_current == 'y':
        num1 = current_total
    elif calc_current == 'n':
        num1 = float(input("What's your first number? "))
