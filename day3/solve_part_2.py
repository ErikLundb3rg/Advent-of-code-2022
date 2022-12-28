def getLines(fileName):
    with open(fileName) as f:
        return f.read().splitlines()


def main():
    lines = getLines('input.in')

    total = 0

    i = 0
    while i < len(lines):
        p1 = lines[i]
        p2 = set(lines[i+1])
        p3 = set(lines[i+2])

        for item in p1:
            if item in p2 and item in p3:
                toAdd = ord(item)-38 if item.isupper() else ord(item)-96
                total += toAdd
                break
        i += 3

    print(total)


if __name__ == '__main__':
    main()
