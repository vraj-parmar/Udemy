with open("vegetables.txt", "w") as my_file:
    my_file.write("tomato\ncucumber\nonion\n")
    my_file.write("garlic")

with open("vegetables.txt", "a+") as my_file:
    my_file.write("\nocra")
    my_file.seek(0)
    content = my_file.read()

print(content)