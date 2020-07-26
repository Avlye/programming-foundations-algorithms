items = [6, 20, 8, 19, 56, 23, 87, 41, 49, 53]


def find_item(item, itemlist):
    for i in itemlist:
        if item == i:
            return i

    return None


print(find_item(87, items)) # Should be 87
print(find_item(250, items)) # Should be None