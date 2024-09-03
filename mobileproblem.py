mobile_price = int(input("enter the mobile price"))
powerbank_purchased = True  
discount_percentage = 0.25 if powerbank_purchased else 0.05
discount_amount = mobile_price * discount_percentage
discounted_price = mobile_price - discount_amount
print("Discount amount:", discount_amount)
print("Discounted price:", discounted_price)
