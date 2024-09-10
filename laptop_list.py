# Suppose you want to purchase a laptop from electronic shop. Perform following operations with the help of List:
# a. Display List of laptop with price
# b. Calculate Price of according to total no. of laptop purchased by customer.
# c. Display updated List of laptop with price

laptop_list = [["Dell", 50000], ["HP", 45000], ["Lenovo", 40000], ["Asus", 35000], ["Acer", 30000]]

print("List of Laptops: ")
for i in range(len(laptop_list)):
    print(f"{i + 1}. {laptop_list[i][0]} : {laptop_list[i][1]}")

total_price = 0

num_laptops = int(input("Enter the number of different laptops you want to purchase: "))

for _ in range(num_laptops):
    laptop_index = int(input("Enter the laptop number (1-5): ")) - 1
    quantity = int(input(f"Enter the quantity for {laptop_list[laptop_index][0]}: "))
    total_price += laptop_list[laptop_index][1] * quantity

print("Total Price of Laptops: ", total_price)

print("\nUpdated List of Laptops with Price: ")
for i in range(len(laptop_list)):
    print(laptop_list[i][0], ":", laptop_list[i][1])
print("\nTotal Price of Laptops: ", total_price)
