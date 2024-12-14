
from utils.utils import sort
from itertools import groupby
# import functools

# def findNumber(item:str):

#     num= ''
#     for i in item:
       
#         if (i.isnumeric()):
#             num += i
#             break

#     for i in (item[::-1]):
#         if (i.isnumeric()):
#             num += i
#             break
        
#     return num
list1:list[int]=[]
list2:list[int]=[]

def group_list(lst):
    x={}
    for el, group in groupby(sorted(lst)):
        x[el] = len(list(group))
            
    # print(x)
    return x
 

def part1(list1: list[str],list2: list[str]):
    total = 0
    sort(list1, False)
    sort(list2, False)
        
    for i, item in enumerate(list1):
        diff = abs(item - list2[i])
        total+=diff
    
    return total


def part2(list1: list[str],list2: list[str]):
#    dict1 = group_list(list1)
   dict2 = group_list(list2)
   total=0
   for x in list1:
       if(dict2.get(x)!=None):
           total+= x*dict2.get(x)
        # total+=pow(x, dict2.get(x))
    
   print(total)

        
def solution(input: list[str]):
    
    for item in input:
        x=item.split('   ')
        list1.append(int(x[0]))
        list2.append(int(x[1]))

        
    part2(list1, list2)
    # print(part1(list1, list2))
   
    # print(functools.reduce(lambda a, b: int(a)+int(b), arr))

      