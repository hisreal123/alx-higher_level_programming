#!/usr/bin/python3
if __name__ == "__main__":
    # import dis
    from calculator_1 import add, sub

    def magic_calculation(a, b):
        if a < b:
            add(a, b)
