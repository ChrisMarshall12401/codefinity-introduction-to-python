# Dictionary of products with price and quantity sold as strings
products = {
    "Apple": ["1.20", "50"],   # "Item": [price, quantity sold]
    "Banana": ["0.50", "100"],
    "Cherry": ["2.50", "25"],
    "Mango": ["1.75", "40"]
}
total_sales_list = []
for item in products:
    #print(item)
    #print(products[item][0],products[item][1])
    subtotal=float(products[item][0])*int(products[item][1])
    #print (subtotal)
    total_sales_list.append(subtotal)
    print(f"Total Sales for {item}: ${subtotal}")

#print(total_sales_list)

total_sum=sum(total_sales_list)
min_sales=min(total_sales_list)
max_sales=max(total_sales_list)
print(f"Total Sum of All Sales: ${total_sum}")
print(f"Minimum sales: ${min_sales}")
print(f"Maximum sales: ${max_sales}")