tup = (87, 64, 33, 95, 76)
print(tup[0])     # 87
print(tup[:3]) # (87, 64, 33)

print(tup[-3:-1]) #(87, 64, 33)

print(tup.count(10)) #0

print(tup.index(33)) #2

# Tuple Examples

# t1 = ()              # Empty tuple
# t2 = (1,)            # Single element tuple (comma required)
# t3 = ("Samosa", "Pizza", "Burger")

# Immutable Nature
# tup = (10, 20, 30)
# tup[0] = 100    # ❌ Error - cannot modify tuples

# Create a tuple of your favorite 5 fruits.
# Then print:
# The total number of fruits
# The index of one selected fruit



fruits = ("Mango", "Apple", "Banana", "Grapes", "Orange")

print("length of furits",len(fruits))

print(fruits.index("Mango")) # 0