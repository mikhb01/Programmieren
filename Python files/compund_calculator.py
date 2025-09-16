# Python combound interest calculator

# Formular for interest: A = P(1+r/n)ᵗ 
# A = Final amount
# P = initial principal balance 
# r = interest rate
# t = number of time periods elapsed

principle = 0
rate = 0
time = 0


while True: 
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("The principle can't be less than or equal to zero!")
    else: 
        break

while True: 
    rate = float(input("Enter the interest rate amount: "))
    if rate <= 0:
        print("The interest rate can't be less than or equal to zero!")
    else:
        break

while True: 
    time = float(input("Enter the time in years: "))
    if time <= 0:
        print("Time can't be less than or equal to zero!")
    else: 
        break

# print(principle)
# print(rate)
# print(time)

total = principle * pow((1 + rate / 100), time)

print(f"Balance after variable {time} year/s: €{total:.2f}")