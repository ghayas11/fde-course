# Demo 1
# 01
with open("shopping.txt","w") as file:
    file. write("Rice\n")
    file.write("Wheat\n")
    file.write("Sugar\n")
    file.write("Salt\n")

with open("shopping.txt","r") as file:
    for index,line in enumerate(file):
        print(f"{index+1}:{line.strip()}")

# 02
def add_note(text):
    with open("log.txt","a")as file:
        file.write(text + "\n")

add_note("Banana")
add_note("Mango")
add_note("Apple")

# 03
with open("sales.txt", "w") as file:
    file.write("18500\n")
    file.write("22300\n")
    file.write("19000\n")
    file.write("31000\n")

with open("sales.txt", "r") as file:
    weekly_total = 0
    count = 0
    for line in file:
        weekly_total += int(line.strip())
        count += 1

weekly_average = weekly_total / count

print(f"Weekly Total: {weekly_total}")
print(f"Weekly Average: {weekly_average:.2f}")

#04
orders = []

with open("orders.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:         
            continue
        order_id, customer, total, status = line.split(",")
        orders.append({
            "id": order_id,
            "customer": customer,
            "total": int(total),
            "status": status,
        })

delivered = [o for o in orders if o["status"] == "delivered"]
delivered_total = sum(o["total"] for o in delivered)

print(f"{len(delivered)} delivered orders, Rs {delivered_total:,}")

#05
orders = []

with open("orders.txt", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
        order_id, customer, total, status = line.split(",")
        orders.append({
            "id": order_id,
            "customer": customer,
            "total": int(total),
            "status": status,
        })

totals = {}
for order in orders:
    if order["status"] == "cancelled":
        continue
    name = order["customer"]
    totals[name] = totals.get(name, 0) + order["total"]

grand_total = sum(totals.values())

with open("report.txt", "w") as file:
    file.write("Order report\n")
    for name, amount in totals.items():
        file.write(f"{name}: Rs {amount:,}\n")
    file.write(f"Total: Rs {grand_total:,}\n")




