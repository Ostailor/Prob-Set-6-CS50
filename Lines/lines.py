import sys

amount_of_lines = 0

try:
    if len(sys.argv) == 1:
        sys.exit('Too few command-line arguments')
    elif len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    elif (sys.argv[1][-3:]) != '.py':
        sys.exit("Not a Python file")
    else:
        with open(sys.argv[1]) as file:
            lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")
else:
    for line in lines:
        if line.strip().startswith('#'):
            continue
        elif line.startswith('\n'):
            continue
        elif line.isspace():
            continue
        else:
            amount_of_lines += 1

print(amount_of_lines)

