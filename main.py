file_input = input("What weather file would you like to open?\n")
user_input = input("Enter what you want to see in this format\n(Max/Min) (Data Type) (Beginning Date) (End Date)\n")

data = []

with open(file_input, 'r') as file:
    for line in file:
        line = line.strip()
        data.append(line)

print(data, "\n")

data[1] = data[1].split(" ")
for i in range(1, len(data)):
    data[1][i] = float(data[1][i])


print(data[1])
