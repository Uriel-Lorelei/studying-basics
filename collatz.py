def collatz(number):
    if number % 2 != 0:
        number = number * 3 +1
    else:
        number = number // 2
    return number

while True: 
    try:
        request_number = int(input("Enter the number: "))
        while request_number != 1:
            request_number = collatz(request_number)
            print(request_number, end=' ')
        break
    except ValueError:
        print("Please enter a number!")

print("")