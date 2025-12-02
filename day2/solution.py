import re

# def part2:


# def part1(password):
#     return password


# def part2(password, additional):
#     return password + additional


def solution(input: str):
    ranges = input[0].split(",")
    total = 0
    for rng in ranges:
        lower, upper = rng.split("-")
        for x in range(int(lower), int(upper) + 1, 1):
            length = len(str(x)) // 2
            first_half = str(x)[:length]
            second_half = str(x)[length:]
            if first_half == second_half:
                total = total + x

    print(total)
