import importlib
from input import openFile

day = "day4"
path = f"{day}"
dayModule = importlib.import_module(f"{path}.solution")
contents = openFile(f"{path}/input.txt")

dayModule.solution(contents)
