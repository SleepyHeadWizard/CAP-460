'''Scenario: A store offers discounts: 10% for clothing and 15% for electronics. Write a function apply_discount(item_type, price) that calculates the final price by calling an inner function get_discount() to retrieve the discount rate based on item_type.'''

while True:
    item_type = input("Enter the item type (clothing/electronics): ")
    price = float(input("Enter the price: "))

    def apply_discount(item_type, price):
        def get_discount(item_type):
            if item_type == 'clothing':
                return 0.1
            elif item_type == 'electronics':
                return 0.15
            else:
                return 0

        global discount
        discount = get_discount(item_type)

        return price - price * discount

    print(f'The final price for the {item_type} is ${apply_discount(item_type, price)} with discount of {int(discount*100)}%')
