with open("data/cities.csv", "r") as f:
    lines = f.readlines()[1:] # Skips header row

total = 0
for line in lines:
    name, population = line.split(",")
    total += int(population)

print(f"Total population: {total:,}")
print(f"Average population: {total / len(lines):,}")

#Try adding comment --> 1


#Imagine paying 75$ for COD
#And not having the PS4 at home xD
#THis is Bart btw