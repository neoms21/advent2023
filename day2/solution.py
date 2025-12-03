import re

# def part2:


def part1(ranges):
    total = 0
    for rng in ranges:
        lower, upper = rng.split("-")
        for x in range(int(lower), int(upper) + 1, 1):
            length = len(str(x)) // 2
            first_half = str(x)[:length]
            second_half = str(x)[length:]
            if first_half == second_half:
                total = total + x

    return total


def part2(ranges):
    total = 0
    for rng in ranges:
        lower, upper = rng.split("-")
        for line in range(int(lower), int(upper) + 1, 1):

            n = len(str(line)) // 2
            # print(f"==>> n: {line}")

            for l in range(n):
                # print(f".   ==>> l: {l}")
                split = [
                    str(line)[i : (i + l + 1)]
                    for i in range(0, len(str(line)), (l + 1))
                ]
                is_match = all(x == split[0] for x in split)
                if is_match:
                    total = total + line
                    break

    return total


def solution(input: str):
    ranges = input[0].split(",")

    # print(part1(ranges))
    print("Total", part2(ranges))
