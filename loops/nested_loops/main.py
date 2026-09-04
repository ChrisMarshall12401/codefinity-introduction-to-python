produce = ["Tomatoes", "Lettuce"]
dairy = ["Milk", "Cheese"]
groceries=[produce,dairy]
print(groceries)
for section in groceries:
    for item in section:
        print ("Item Name: ",item)