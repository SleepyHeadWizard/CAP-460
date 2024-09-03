'''a grocery store offer a discount based on total purchase amount.
write a program that takes the total amount of purchase as input and calculate the discount based on the following criteria:
Total purchase amount	Discount
above 100	10%
above 200	20%
anything above 300	25%'''

total_purchase = float(input("Enter the total purchase amount: "))
discount = 0
if total_purchase > 300:
    discount = 0.25
elif total_purchase > 200:
    discount = 0.20
elif total_purchase > 100:
    discount = 0.10


print(f"Discount: {discount * 100}%")
print(f"final amount: {total_purchase - total_purchase * discount}")


