import spinput
import spdraw
import spcalc

inp = spinput.read_input("input.txt")
out = spcalc.calculate(inp)
spdraw.draw(out)
