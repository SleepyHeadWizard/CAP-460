cars = {
    "MarutiCar": (400000, 600000, 12),
    "FordCar": (600000, 700000, 13),
    "HundaiCar": (700000, 800000, 14)
}

budget = 700000

best_car = None
best_price = None

for car, (min_price, max_price, offer) in cars.items():
    if min_price <= budget <= max_price:
        price_after_discount = max_price - (max_price * offer / 100)
        if best_price is None or price_after_discount < best_price:
            best_car = car
            best_price = price_after_discount

if best_car:
    print(f"Recommended car: {best_car}")
else:
    print("No car available within the budget.")
