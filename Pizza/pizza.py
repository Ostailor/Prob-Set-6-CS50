from tabulate import tabulate
import csv
import sys

pizzas = []
try:
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            pizzas.append(row)
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    print(tabulate(pizzas, headers="keys", tablefmt='grid'))
