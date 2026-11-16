#DEMO 4
#1

total = 6200
city = "Lahore"
if total>= 5000 and city == "Lahore":
    print("Free Delivery")
else:
    print(" Delivery Charge: Rs 350.")

#2
marks =50
if marks >=80 and marks <= 100:
    print("A Grade")
elif marks >= 65 and marks<= 79:
    print(" B Grade")
elif  marks >= 50 and marks <= 64:
    print("C Grade")
elif marks < 50 and marks >0:
    print("Fail")
else:
    print("Invalid Option")

#3
quantity = 5
stock =12
if quantity <= 0:
    print("invalid Quantity")
elif quantity > stock:
    print("Only 12 left in stock") 
else:
    purchased = stock - quantity
    print(f"Confirmed. only {purchased} left after this order")

#4
weight_kg = 3
order_total = 2000
city = " karachi "
city = city.strip().title()
if order_total > 10000:
    charge = 0
elif city in ["Karachi", "Lahore", "Islamabad"]:
    charge = 200 if weight_kg <= 5 else 400
else:
    charge = 350 if weight_kg <= 5 else 700
print(f"Shipping to {city}: Rs {charge}")

#5

plan = "pro"
hours_open = 30
message = "I was CHARGED TWICE for my subscription"

text = message.lower()

if plan == "enterprise" and hours_open > 4:
    print("Urgent")
elif "refund" in text or "charged twice" in text or (plan == "pro" and hours_open > 24):
    print("High")
else:
    print("Normal")