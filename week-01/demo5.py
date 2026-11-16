#DEMO 5
#1
orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "delivered"},
]
total_deliveries =0
for order in orders:
    if order["status"] == "delivered":
        total_deliveries += order["total"]
print(f"Delivered revenue: Rs{total_deliveries:,d}.")
    
#2
prices = [850, 1200, 400, 3100, 650]
count = 0
counterb =0
for index,price in enumerate (prices):
    count+=price    
    print(f"Item {index}:Rs {price:,}")
    if price>1000:
     counterb +=1
print(f"Total sale above 1000 are: {counterb}")
print(f"Total price: {count:,}.")

#3
orders = [
    {"id": "A101", "total": 4500, "status": "delivered"},
    {"id": "A102", "total": 12800, "status": "pending"},
    {"id": "A103", "total": 2300, "status": "delivered"},
]
highest_num =0
highest_order = None
for order in orders:
    if order["total"] >highest_num:
        highest_num =order["total"]
        highest_order = order["id"]
print(f"Biggest order: {highest_order} (Rs {highest_num:,}).")

#4
orders = [
    {"customer": "Noor Foods", "total": 4500},
    {"customer": "Karachi Crafts", "total": 12800},
    {"customer": "Noor Foods", "total": 2300},
    {"customer": "Bilal Traders", "total": 7600},
    {"customer": "Karachi Crafts", "total": 3900},
    {"customer": "Noor Foods", "total": 6100},
]

totals = {}
for order in orders:
    name = order["customer"]
    if name in totals:          
        totals[name] += order["total"]
    else:
        totals[name] = order["total"]

for customer, amount in totals.items():
    print(f"{customer}: Rs {amount:,}")

#5
inventory = [
    {"name": "Notebook", "stock": 8, "reorder_level": 15, "unit_cost": 90},
    {"name": "Pen", "stock": 140, "reorder_level": 50, "unit_cost": 25},
    {"name": "Stapler", "stock": 2, "reorder_level": 5, "unit_cost": 650},
    {"name": "Marker", "stock": 30, "reorder_level": 30, "unit_cost": 120},
    {"name": "Folder", "stock": 11, "reorder_level": 20, "unit_cost": 60},
]


def build_reorder_report(items):
    lines = []
    total_cost = 0
    for item in items:
        if item["stock"] < item["reorder_level"]:
            qty = 2 * item["reorder_level"] - item["stock"]
            cost = qty * item["unit_cost"]
            total_cost += cost
            lines.append(f"Reorder {qty} x {item['name']} (Rs {cost:,})")
    if not lines:
        return ["All stock OK"]
    lines.append(f"Total cost: Rs {total_cost:,}")
    return lines


for line in build_reorder_report(inventory):
    print(line)


all_ok = [dict(item, stock=item["reorder_level"] + 1) for item in inventory]
for line in build_reorder_report(all_ok):
    print(line)
