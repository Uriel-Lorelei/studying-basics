def apa(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('no divide by 0 bitte')
print(apa(0))