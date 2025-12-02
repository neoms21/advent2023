import re

# def part2:


def calculate_next_point(direction, distance, starting_point):

    final_point = 0
    additional = 0
    if direction == "L":
        x = starting_point - distance
        if x < 0:
            final_point = x + 100
            if starting_point != 0:
                additional = 1
        else:
            final_point = x
    else:
        x = starting_point + distance
        if x >= 100:
            final_point = x - 100
            if final_point != 0:
                additional = 1
        else:
            final_point = x
    return {"final_point": final_point, "additional": additional}


def part1(password):
    return password


def part2(password, additional):
    return password + additional


def solution(input: list[str]):
    password = 0
    next_point = 50
    additional = 0
    for code in input:
        direction = re.search("\w{1}", code)
        distance = int(re.search("\d{1,4}", code)[0])
        full_turns = distance // 100
        remaining = distance % 100

        abs_distance = remaining if distance > 100 else distance

        result = calculate_next_point(direction[0], abs_distance, next_point)
        next_point = result.get("final_point")
        additional = additional + full_turns + result.get("additional")
        # print(f"==>> result: {additional}")
        # additional = full_turns + additional

        if next_point == 0:
            password = password + 1

    print(part1(password))
    print(part2(password, additional))
