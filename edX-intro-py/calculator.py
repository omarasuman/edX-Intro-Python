# calculator asking user for input

x = float(input("what's x? "))
y = float(input("what's y? "))

# rouding to get rid of decimals
z = round(x + y)
# and printing the addition of the input
print(f"{z:,}")
