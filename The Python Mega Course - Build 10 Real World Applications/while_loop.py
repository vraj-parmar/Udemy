# Method 1
username = ""

while username != "pypy":
    username = input("Enter username: ")

# Method 2 (better one)
while True:
    username = input("Enter username: ")
    if username == "pypy":
        break
    else:
        continue