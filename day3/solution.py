
from utils.utils import sort
from itertools import groupby
import re


def part1(input:str):
    x = re.findall("mul\(\d+,\d+\)", input)
    total=0
    # print(len(x),x)
    for m in x:
        strs = re.findall("\d+", m)
        nums = [int(a) for a in strs]
        total+=nums[0]*nums[1]
    
    # print(total)
    return total

    

def solution(input: str):
    part1(input[0])
    
    
    # # res_dont = [i.start() for i in re.finditer("don't\(\)", input[0]) ]
    # # res_do = [i.start() for i in re.finditer("do\(\)", input[0]) ]
    # # print('DONT',res_dont)
    # # print('DO', res_do)
    # # part2(list1, list2)
    # # print(part1(list1, list2))
   
    # # print(functools.reduce(lambda a, b: int(a)+int(b), arr))
    # inp =input[0]
    # part2_total = 0
    # indices = ['0,349']
    # for ind in indices:
    #     bounds=ind.split(',')
    #     sub_str=inp[int(bounds[0]):int(bounds[1])]
    #     # print(sub_str)
    #     # print('------')
    #     part2_total+=part1(sub_str)
    # # print(part2_total)
    
    
    # x = re.findall("do\(\).*?don\'t\(\)", input[0])

    # for st in x:    
    #     part2_total+=part1(st)
    
    # print(part2_total)
    
    res = 0
    do = True
    for i, j, k in re.findall("(mul\((\d+),(\d+)\)|do\(\)|don't\(\))", input[0]):
        print(i,j,k)
        if i == "don't()":
            do = False
        elif i == "do()":
            do = True
        else:
            if do or False:
                res += int(j) * int(k)
    print(res)


    
    # print(4560547+99581491)
    