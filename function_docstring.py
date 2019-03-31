def print_max(x, y):
    ''' Prints the maximum of two numbers.
    The two values must be integer'''
    # convert to integers, if possible
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    elif y > x:
        print(y, 'is maximum')
    else:
        print('equal')

print_max(3, 5)
print(print_max.__doc__)