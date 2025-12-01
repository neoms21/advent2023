from utils.utils import sort
from itertools import groupby
import re


def calculate_next_point(direction, distance, starting_point):

    if direction == "L":
        x = starting_point - distance
        if x < 0:
            return x + 100
        else:
            return x
    else:
        x = starting_point + distance
        if x >= 100:
            return x - 100
        else:
            return x


def solution(input: list[str]):
    password = 0
    next_point = 50
    for code in input:
        direction = re.search("\w{1}", code)
        distance = re.search("\d{1,4}", code)
        abs_distance = (
            int(distance[0]) % 100 if int(distance[0]) > 100 else int(distance[0])
        )
        next_point = calculate_next_point(direction[0], abs_distance, next_point)
        if next_point == 0:
            password = password + 1

    print(password)
