def maximum(x, y):
    if x > y:
        return x
    if x < y:
        return y
    if x == y:
        return 'the number is equal'

print(maximum(3,3))