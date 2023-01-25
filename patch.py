# patch.py
import sys

def patch(file, diff):
    with open(file, 'r') as f:
        lines = f.readlines()

    for i, d in enumerate(diff):
        op, line = d
        if op == '-':
            lines.pop(i)
        elif op == '+':
            lines.insert(i, line)

    with open(file, 'w') as f:
        f.writelines(lines)

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python patch.py file diff")
        sys.exit(1)

    file, diff_file = sys.argv[1:]
    with open(diff_file, 'r') as f:
        diff = f.read()
    patch(file, diff)
