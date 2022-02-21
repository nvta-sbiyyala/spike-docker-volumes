import sys


def main(argv):
    with open('data/input.txt') as input_file:
        lines = input_file.readlines()
        output = "".join(lines).upper()

    with open('data/output.txt', 'w') as output_file:
        output_file.write(output)
        output_file.close()


if __name__ == "__main__":
    sys.exit(main(sys.argv))
