# def part2(ranges):
#     total = 0
#     for rng in ranges:
#         lower, upper = rng.split("-")
#         for line in range(int(lower), int(upper) + 1, 1):
#
#             n = len(str(line)) // 2
#             # print(f"==>> n: {line}")
#
#             for l in range(n):
#                 # print(f".   ==>> l: {l}")
#                 split = [
#                     str(line)[i : (i + l + 1)]
#                     for i in range(0, len(str(line)), (l + 1))
#                 ]
#                 is_match = all(x == split[0] for x in split)
#                 if is_match:
#                     total = total + line
#                     break
#
#     return total

# i == 0  and previous_index == -1:
#             first_battery = num
#             first_index = i
#         elif

def find_battery(arr, selected_index):
    # print("sel", selected_index, arr)
    first_battery = 0
    first_index = 0
    for i, num in enumerate(arr):
        if num > first_battery and i >= selected_index:
            first_battery = num
            first_index = i
        else:
            continue
    return first_battery, first_index


def solution(contents: str):
    batteries_to_find = 2
    counter = 0
    total = 0
    for line_index, line in enumerate(contents):
        cells = ''
        nums = [int(e) for e in [*line]]

        first_battery = find_battery(nums,-1)
        # print(first_battery)
        selected_index = -1 if (first_battery[1] == len(nums)-1) or (first_battery[1] == 0) else first_battery[1]
        nums.pop(first_battery[1])
        second_battery = find_battery(nums, selected_index)
        # while counter < batteries_to_find:
        #
        #     print(batteries)
        #     counter = counter + 1


        sorted_by_second = sorted([first_battery, second_battery], key=lambda tup: tup[1])
        for x in sorted_by_second:
            cells = cells + str(x[0])
        print(line_index, int(cells))
        total = total + int(cells)
    print(f"total: {total}")