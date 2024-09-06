import sys


def count_spaces(text):
    for line in text.split("\n"):
        c = 0
        for ch in line:
            if " " == ch:
                c += 1
        print(line, c)


if __name__ == "__main__":
    if not sys.stdin.isatty():
        input_text = sys.stdin.read()
    else:
        if len(sys.argv) != 2:
            print("Usage: python3 space_count.py 'text'")
            sys.exit(1)

        input_text = sys.argv[1]

    count_spaces(input_text)
