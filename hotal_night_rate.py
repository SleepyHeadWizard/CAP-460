'''Scenario: A hotel charges a fixed rate of $100 per night, plus a cleaning fee of $20. Write a function calculate_total_cost(nights) that calculates and returns the total cost for a stay based on the number of nights booked.
Bonus: Modify the function to accept an optional parameter for a discount percentage (applied only to the nightly rate).'''
while True:
    stay = int(input('number of night you want to stay: '))
    discount = int(input('Enter the discount percentage: '))

    def calculate_total_cost(nights, discount=0):
        night_rate = 100
        cleaning_fee = 20
        total = (night_rate * nights) + cleaning_fee
        if discount:
            total -= total * discount / 100
        return total

    print(f'The total cost for {stay} nights is ${calculate_total_cost(stay, discount)}')

