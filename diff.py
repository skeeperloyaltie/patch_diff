# diff.py
import sys

def diff(file1, file2):
    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    diff = []
    for i in range(max(len(lines1), len(lines2))):
        try:
            line1 = lines1[i]
        except IndexError:
            diff.append(('+', lines2[i]))
            continue
        try:
            line2 = lines2[i]
        except IndexError:
            diff.append(('-', lines1[i]))
            continue
        if line1 != line2:
            diff.append(('-', line1))
            diff.append(('+', line2))

    return diff

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python diff.py file1 file2")
        sys.exit(1)

    file1, file2 = sys.argv[1:]
    print(diff(file1, file2))
