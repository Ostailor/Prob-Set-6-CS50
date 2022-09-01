import csv
import sys

people = []

try:
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) < 2:
        sys.exit("Too many command-line arguments")
    else:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            for row in reader:
                people.append(row)
except FileNotFoundError:
    sys.exit("Could not read", sys.argv[1])
else:
    after = []

    for i in range(len(people)):
        Last, First = people[i].get('name').split(",")
        posting = {"first": First[1:], "last": Last, "house": people[i].get('house')}
        after.append(posting)
    with open(sys.argv[2], "w") as file:
        writer1 = csv.DictWriter(file, fieldnames=["first", "last", "house"])
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"]).writeheader()
        for i in range(len(after)):
            writer1.writerow(after[i])
