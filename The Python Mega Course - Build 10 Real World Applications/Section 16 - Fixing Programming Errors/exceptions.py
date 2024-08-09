# a = 1
# b = "2"
# c = 3
# print(int(2.5))
# print(c/0)

def divide(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        return("Zero division is not possible")

print(divide(0,0))