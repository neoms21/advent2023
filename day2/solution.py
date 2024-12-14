
from utils.utils import sort
from itertools import groupby

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
    safes=0
    for item in input:
        nums= [ int(x) for x in item.split(' ')]
        diff:int = None
        prevNum:int = None
        arr=[]
        
        for i, num in enumerate(nums):
            # print(prevNum)
            if(diff == None):
              diff = 0
              prevNum = num
              continue
            if(prevNum-num>0):
                arr.append('I')
            else:
                arr.append('D')
                
            diff = abs(prevNum - num)
           
            prevNum = num
            if(diff<1 or diff>3 or len(set(arr))>1):
                # print('UNSAFE', nums)
                diff = None
                prevNum = None
                break

            if(i== len(nums)-1):
                safes+=1
        
    print(safes)

        
    # part2(list1, list2)
    # print(part1(list1, list2))
   
    # print(functools.reduce(lambda a, b: int(a)+int(b), arr))

      