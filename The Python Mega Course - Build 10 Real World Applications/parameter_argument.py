# non-keyword arguments
def mean(*args):
    return sum(args) / len(args)

print(mean(1, 3, 4))

# keyword arguments
def mean(**kwargs):        # type of kwargs = dictionary
    return kwargs

print(mean(a=1, b=2, c=3))


# input: indefinite list of strings
# output: alphabetically sorted and upper case list

def sort_upper(*args):
    return sorted(item.upper() for item in args)

print(sort_upper("snow", "glacier", "iceberg"))