'''You have a dictionary representing items in stock at two different stores. Write a function that compares the inventories and returns a list of items that are present in the first store but missing in the second store.'''

shop1 = {'item1': 45, 'item2': 35, 'item3': 20, 'item4': 10, 'item5': 5}
shop2 = {'item1': 45, 'item2': 35, 'item4': 10}

missing_items = []
for i in shop1:
    if i not in shop2:
        missing_items.append(i)
print(missing_items)
        