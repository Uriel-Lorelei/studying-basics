def box(symbol, width, height):
    if len(symbol) != 1:
        raise Exception("the symbol should be one character string") 
    if width <= 2:
        raise Exception("the width should be greater than 2")
    if height <= 2:
        raise Exception("the height should be greater than 2")


    # symbol = input("SYMBOL: ")
    # width = int(input("Please put a number for width: "))
    # height = int(input("Please put a number for height: "))

    print((symbol + " ") * width)
    for i in range(height - 2):
        print(symbol + (" " * width) + symbol)
    print((symbol + " ") * width)

try:
    box('E', 3, 3)
    box('SS', 2, 1)
    box('@', 3, 6)
    box('54', 3, 3)
except Exception as err:
    print("Etwas schlecht hat passiert: " + str(err))