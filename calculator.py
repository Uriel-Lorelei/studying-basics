
def add(x, y):
    return (x + y)
    
def subtract(x, y):
    return (x - y)

def multiply(x, y):
    return (x * y)

def divide(x, y):
    try:
        return (x/y)
    except ZeroDivisionError:
        print("Don't divide by 0 bitte.")

def power(x, y):
    return x ** y
    
def square_root(x):
    return x ** (1/2)

def cube_root(x):
    return x ** (1/3)

def percentage(x, y):
    return x * (y/100)

def calculator():
    try:
        num1 = int(input("A number please: "))
        sign = input("What would you like to do?\n1. Add(+)\n2. Subtract(-)\n3. Multiply(*)\n4. Divide(/)\n5. Exponential(p)\n6. Square root(s)\n7. Cube root(c)\n8. Percentage(%)\n> ").lower()
        
        if sign == "s":
            print(square_root(num1))
        elif sign == "c":
            print(cube_root(num1))
        else:
            num2 = int(input("Another number: "))

            if sign == "+":
                print(add(num1, num2))
            elif sign == "-":
                print(subtract(num1, num2))
            elif sign == "*":
                print(multiply(num1, num2))
            elif sign == "/":
                print(divide(num1, num2))
            elif sign == "p":
                print(power(num1, num2))
            elif sign == "%":
                print(percentage(num1, num2))
            else:
                user_ans = input("Did you add the correct symbol? (y/n): ").lower()
                if user_ans == "y" or "yes":
                    print(f"No, you used {sign}! TRY AGAIN!")
                    calculator()
                elif user_ans == "n" or "no":
                    print("Good thing that you recognize your mistakes. TRY AGAIN.")
                    calculator()
                else:
                    print("No wonder. You can't even do a simple yes or no.")
    except ValueError:
        print("Did you use something else other then a NUMBER?")
    except KeyboardInterrupt:
        print("\nOh no! Maybe you tried to do a super large number? Or... or.. do you j-just hate me...?")

calculator()