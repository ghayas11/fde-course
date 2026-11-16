#Demo 3
#1
prices =[850,1200,400]
print(f"Last price {prices[-1]}")
print(f"Sum of all {sum(prices)}")

#2
product ={"name":"Ice_cream","price":1000,"in_stock":True }
product["in_stock"]=False
print(f"Product Name:{product["name"]}")
print(f"Is it available? {product['in_stock']}")

#3
weekly_list = [18500, 22300, 19800, 25400, 31200, 42800, 38600]
weekly_total =sum(weekly_list)
daily_average = weekly_total/len(weekly_list)
worst_day =min(weekly_list)
Best_sale = max(weekly_list)
print(f"The Monday sale is Rs: {weekly_list[0]:,.0f} and sunday sale is Rs: {weekly_list[-1]:,.0f}.")
print(f"Weekly total is Rs: {weekly_total:,.0f} and Weekly average is Rs: {daily_average:,.0f}. ")
print(f"Worst day sale is Rs: {worst_day:,.0f} and Best day sale is Rs: {Best_sale:,.0f}.")

#4
stock_counts = {"pens": 120, "notebooks": 45, "staplers": 8}
stock_counts["notebooks"]==15
stock_counts["markers"]=60
print(len(stock_counts))
print(stock_counts)
print(*stock_counts)

#5
customer = {
    "name": "Noor Foods",
    "address": {"city": "Karachi", "area": "Clifton"},
    "order_totals": [4500, 12800, 2300],
}
phone =customer.get("phone")

print(f"The city is {customer["address"]["city"]}.")
print(f"The total amount spent is Rs: {sum(customer['order_totals'])}")
print(f"The Number of phones is: {phone}")