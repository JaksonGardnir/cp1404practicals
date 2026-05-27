"""
Program that estimates your electricity bill.
"""

TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity bill estimator 2.0")
tariff_number = int(input("Which tariff? 11 or 31: "))
while tariff_number != 11 and tariff_number!= 31:
    print("Invalid tariff number.")
    tariff_number = int(input("Which tariff? 11 or 31: "))
daily_use_kWh = float(input("Enter daily use in kWh: "))
number_of_billing_days = int(input("Enter number of billing days: "))
if tariff_number == 11:
    estimated_bill = TARIFF_11 * daily_use_kWh * number_of_billing_days
else:
    estimated_bill = TARIFF_31 * daily_use_kWh * number_of_billing_days
print(f"Estimated bill: ${estimated_bill:.2f}")
