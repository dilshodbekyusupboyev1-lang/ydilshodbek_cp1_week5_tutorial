def classify(weight):
    if weight < 1998:
        return "Below range"
    elif weight <= 2002:
        return "In range"
    else:
        return "Above range"
def calculate_average(total, count):
    return total / count
num_bags = int(input("Enter the number of flour bags:"))
x = 0
y = 0
z = 0
total = 0
for a in range(num_bags):
    weight = int(input("Enter the flour bag weight:"))
    category = classify(weight)
    print(category)
    if category == "Below range":
        x += 1
    elif category == "In range":
        y += 1
    elif category == "Above range":
        z += 1
    total += weight
avg = calculate_average(total, num_bags)
print(f"Total weight: {total} g")
print(f"Average weight: {avg} g")
print(f"Below range: {x}")
print(f"in range: {y}")
print(f"above range: {z}")