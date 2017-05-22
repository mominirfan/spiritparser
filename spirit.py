import csv
with open("spirit.csv", "rb") as file:
	reader = csv.reader(file)
	deals = list(reader)

for line in deals: 
	for element in line:
		if "To:" in element:
			print element