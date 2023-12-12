from input import openFile
import importlib
day= "day8"
dayModule = importlib.import_module(f"{day}.solution")
input = openFile(f"{day}/input.txt")
dayModule.solution(input)