# inventory = {}

# def update_inventory(inventory: dict, name: str, count: int):
#     if name in inventory:
#         inventory[name] += count
#     else:
#         inventory[name] = count


# def get_stock(inventory: dict, name: str):
#    return inventory.get(name, 0)




# update_inventory(inventory, "apple", 10)
# print(get_stock(inventory, "apple"))  # => 10
# update_inventory(inventory, "banana", 5)
# print(get_stock(inventory, "banana"))  # => 5
# update_inventory(inventory, "banana", 2)
# print(get_stock(inventory, "banana"))  # => 7

def sum(x = 5, y = 6):
    print(x - y)


sum(x = 3)
print(sum.__defaults__)