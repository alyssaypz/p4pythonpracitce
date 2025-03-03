groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]

while True:
    print("\nCurrent groceries:", groceries)
    item = input("Enter an item to remove (or type 'stop' to end): ").strip().lower()
    
    if item == "stop":
        break
    elif item in groceries:
        groceries.remove(item)
        print(f"{item} removed from the list.")
    else:
        print(f"{item} is not in the list.")

print("\nFinal groceries list:", groceries)