# method 1
my_file = open("fruits.txt")
content = my_file.read()
my_file.close()

# method 2 (better one)
with open("fruits.txt") as my_file:
    content = my_file.read()


print(content)