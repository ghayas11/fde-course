## 1
name ="aMNA rAZA"
cln_name =name.title()
print(f"welcome{cln_name}! Your nmae has {len(cln_name)} characters")

## 2
email ="Ali.Khan@GMAIL.com "
cln_email =email.lower().strip().replace(" ","")
print(f"Email: {cln_email} ({len(cln_email)} characters)")

##3
name = " wireless MOUSE "
price = 2499
order = 3
total_price =order*price
print(f"{name.title()}x{order} = Rs {"{:,}".format(total_price)}.")

##4
raw_code = " ord-2024-0042 "
print(f"Order{(cln_code:= raw_code.upper().replace("-",""))}has {len(cln_code)} Characters")

##5
first = " bilal"
last = "QURESHI "
city = "lahore"

print(f" Welcome!{(first+" "+last).title()} from {city}\nYour username is {(name:=first+"."+last+"_"+city[0:3]).lower().replace(" ","")} (characters {(len(name))})")


