from input import openFile
import importlib
day= "day1"
path=f"{day}"
dayModule = importlib.import_module(f"{path}.solution")
input = openFile(f"{path}/input.txt")

dayModule.solution(input)