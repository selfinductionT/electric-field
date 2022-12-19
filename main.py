import spinput
import spdraw
import spcalc
import sys


def main():
    input_file = sys.argv[1]
    inp, out = spinput.read_input(input_file)
    field = spcalc.Field(inp)
    field.calc()
    spdraw.draw(field, out, norm=False)


if __name__ == "__main__":
    main()
