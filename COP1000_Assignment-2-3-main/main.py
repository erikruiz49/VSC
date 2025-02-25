# Furniture.py - This program calculates profits and sales prices for a furniture company.

itemName = "TV Stand"
retailPrice = 325.00
wholesalePrice = 200.00
salePrise = retailPrice - (retailPrice * 0.25)
saleProfit = salePrise - wholesalePrice

# Write your assignment statements here for profit, salePrice, and saleProfit

print("Item Name: " + itemName)
print("Retail Price: $" + str(retailPrice))
print("Wholesale Price: $" + str(wholesalePrice))
print("Profit: $" + str(retailPrice - wholesalePrice))
print("Sale Price: $" + str(salePrise))
print("Sale Profit: $" + str(saleProfit))
