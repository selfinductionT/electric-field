import spinput
import spdraw
import spcalc


def main():
    inp = spinput.read_input("input.txt")
    field = spcalc.Field(inp)
    field.calc()
    spdraw.draw(field)


main()
