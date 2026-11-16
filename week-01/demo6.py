##DEMO 6
# ##1
def format_rupees(amount):
    return(f"{amount:,}")
print(f"Noor Foods owes you Rs {format_rupees(128000)}")

# #2
def add_tax(subtotal, rate=0.18):
    return round(subtotal * (1 + rate), 2)

print(add_tax(7200))
print(add_tax(7200, 0.05))
print()

def add_tax_print(subtotal, rate=0.18):
    print(round(subtotal * (1 + rate), 2))

result = add_tax_print(7200)
print(result)
print()


# #3
def shipping_charge(weight_kg, city):
    city_clean = city.strip().lower()
    major_cities = {"karachi", "lahore", "islamabad"}

    if city_clean in major_cities:
        charge = 200
    else:
        charge = 350

    if weight_kg > 5:
        charge *= 2

    return charge

print(f"Shipping to Karachi: {format_rupees(shipping_charge(3, ' karachi '))}")
print(f"Shipping to Lahore: {format_rupees(shipping_charge(6, 'Lahore'))}")
print(f"Shipping to Quetta: {format_rupees(shipping_charge(5, 'Quetta'))}")
print(f"Shipping to Peshawar: {format_rupees(shipping_charge(5.5, 'Peshawar'))}")
print()


# #4
orders = [
    {"id": 1, "status": "delivered", "total": 3400},
    {"id": 2, "status": "delivered", "total": 3400},
    {"id": 3, "status": "pending",   "total": 12800},
]

def total_by_status(orders, status):
    total = 0
    for order in orders:
        if order["status"] == status:
            total += order["total"]
    return total

print("delivered:", total_by_status(orders, "delivered"))
print("pending:  ", total_by_status(orders, "pending"))
print("cancelled:", total_by_status(orders, "cancelled"))
print()


# #5
products = [
    {"name": "Product A", "stock": 5,  "reorder_level": 10, "max_stock": 40, "unit_cost": 120},
    {"name": "Product B", "stock": 2,  "reorder_level": 5,  "max_stock": 20, "unit_cost": 90},
    {"name": "Product C", "stock": 30, "reorder_level": 10, "max_stock": 50, "unit_cost": 75},
    {"name": "Product D", "stock": 8,  "reorder_level": 10, "max_stock": 30, "unit_cost": 120},
    {"name": "Product E", "stock": 6,  "reorder_level": 10, "max_stock": 16, "unit_cost": 46},
]
def format_rupees(amount):
    return f"Rs {amount:,.0f}"

def needs_reorder(product):
    return product["stock"] <= product["reorder_level"]

def reorder_quantity(product):
    return product["max_stock"] - product["stock"]

def reorder_cost(product):
    return reorder_quantity(product) * product["unit_cost"]

total = 0
for product in products:
    if needs_reorder(product):
        qty = reorder_quantity(product)
        cost = reorder_cost(product)
        total += cost
        print(f"{product['name']}: order {qty} for {format_rupees(cost)}")

print("Total:", format_rupees(total))