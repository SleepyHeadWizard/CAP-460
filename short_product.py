'''Task: Write a program that sorts a list of product tuples based on the second element (price) in ascending order. The product tuple consists of the product name and price. The program should print the sorted list of product tuples.'''
# without using lambda function

products = [('laptop', 1000), ('phone', 800), ('watch', 200), ('camera', 500)]
sorted_products = []
for i in range(len(products)):
    for j in range(len(products)):
        if products[i][1] < products[j][1]:
            products[i], products[j] = products[j], products[i]
sorted_products = products
print(sorted_products)