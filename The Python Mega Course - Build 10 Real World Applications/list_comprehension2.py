temps = [221, 234, 340, -9999, 230]

# ignore -9999
new_temps = [temp / 10 for temp in temps if temp != -9999]
print(new_temps)

#replace -9999 with 0
new_temps = [temp / 10 if temp != -9999 else 0 for temp in temps]
print(new_temps)


# def foo(my_list):
#     new_list = [item for item in my_list if isinstance(item, int)]
#     return(new_list)

# print(foo([99, 'no data', 95, 94, 'no data']))