# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "scipy",
# ]
# ///

from scipy.optimize import linprog


def part1(input, add=0):
    c = [3, 1]
    sum = 0
    for equation in input.split("\n\n"):
        parts = equation.strip().split("\n")
        button_a = [int(i.split("+")[1]) for i in parts[0].split(":")[1].split(",")]
        button_b = [int(i.split("+")[1]) for i in parts[1].split(":")[1].split(",")]
        prize = [add + int(i.split("=")[1]) for i in parts[2].split(":")[1].split(",")]
        solution = linprog(
            c,
            A_eq=[[button_a[0], button_b[0]], [button_a[1], button_b[1]]],
            b_eq=prize,
            integrality=1,
            options={"autoscale": True, "presolve": False},
        )
        if solution.success:
            sum += (c[0] * solution.x[0]) + c[1] * solution.x[1]

    return sum


def part2(input):
    return part1(input, add=10000000000000)
