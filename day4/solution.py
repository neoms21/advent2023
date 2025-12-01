from utils.utils import sort
from itertools import groupby
import re


# i-1,j;i+1,j;i,j-1;i,i+1
def solution(input: list[str]):
    total_x = 0

    for i, line in enumerate(input):
        x_indices = [i.start() for i in re.finditer("X", line)]
        for j, x_index in enumerate(x_indices):
            print(f"X={x_index};;neighbours=  {i-1},{j};{i+1},{j};{i},{j-1};{i},{j+1}")
        total_x += line.count("X")

    print(total_x)
