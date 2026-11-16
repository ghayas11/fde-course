# 1
import json
products= {"name":"Laptop","price":80000,"brand":"HP"   }
# Python's print() shows the dictionary using Python syntax
print(products)
# json.dumps() converts it to a single-line JSON string
print(json.dumps(products))

# indent=2 adds line breaks and two-space indentation for readability
print(json.dumps(products, indent=2))


# 2
text = '{"name": "Amna Raza", "plan": "pro", "active": true, "tags": ["vip", "lahore"]}'
data = json.loads(text)  
print(data)
print(data["name"])          
print(len(data["tags"]))    
print(type(data["active"]))  

#3

with open("orders.json") as file:
    loaded = json.load(file)

total = sum(order["total"] for order in loaded)
print(f"{len(loaded)} orders, Rs {total:,} in total")

#4
import json

with open("stock.json") as file:
    stock = json.load(file)

stock["notebooks"] -= 30

if "markers" not in stock:
    stock["markers"] = 60

with open("stock.json", "w") as file:
    json.dump(stock, file, indent=2)

print(stock)
#5
import json

with open("response.json") as file:
    response = json.load(file)

data = response["data"]
customer = data["customer"]
orders = data["orders"]

order_count = len(orders)
item_count = sum(len(order["items"]) for order in orders)
total = sum(order["total"] for order in orders)

print(f"{customer['name']} ({customer['city']}): {order_count} orders, {item_count} items, Rs {total:,}")

summary = {
    "customer": customer["name"],
    "order_count": order_count,
    "item_count": item_count,
    "total": total,
}

with open("summary.json", "w") as file:
    json.dump(summary, file, indent=2)

#Daily task
import json

with open("expenses.json") as file:
    expenses = json.load(file)

for expense in expenses:
    print(f"{expense['item']}: Rs {expense['amount']:,}")

total = sum(expense["amount"] for expense in expenses)
print(f"Total: Rs {total:,}")
