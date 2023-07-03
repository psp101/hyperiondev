menu = ['coke', 'water','sandwich', 'burger'] #items available in the menu
prices = {'coke': 2, 'water': 1, 'sandwich': 3, 'burger' : 4, } # item and price of each item available
stock  = {'coke': 10, 'water': 5, 'sandwich':10, 'burger' : 15,} # item and quantity of stock
total = 0

for key in prices:
     total += prices[key]*stock[key] # stock value of individual item
     print(prices[key] * stock[key])
print ("Total stock value = " , total) #total stock value of the whole menu

