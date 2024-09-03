meter_reading = 120
rate = 6.95 if meter_reading > 100 else 5.95
bill_amount = meter_reading * rate
print("Total electricity bill:", bill_amount)
