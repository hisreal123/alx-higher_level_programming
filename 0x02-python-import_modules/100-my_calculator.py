#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    length = len(sys.argv)

    dice = {"+": add, "-": sub, "*": mul, "/": div}

    if length != 4:
        print("Usage: {} <a> <operator> <b>".format(sys.argv[0]))
        exit(1)

    first_number = int(sys.argv[1])
    second_number = int(sys.argv[3])

    if sys.argv[2] not in dice:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    op = sys.argv[2]
    result = dice[op](first_number, second_number)
    print("{} {} {} = {}".format(first_number, op, second_number, result))
