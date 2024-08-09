name = input("Enter your name: ").title()
surname = input("Enter your surname: ").title()
when = "today"

message = "Hello %s %s!" % (name, surname)
new_message = f"Hello {name} {surname}. What's up {when}" # python3.6 and later

print(message)
print(new_message)