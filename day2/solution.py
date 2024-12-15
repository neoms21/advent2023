
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
 

def check_safe_unsafe(nums):
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
            # return nums
            return 0

        if(i == len(nums)-1):
            return 1

 

def part1(input: list[str]):
    safe_total=0
    unsafes=[]
    for item in input:
        nums= [ int(x) for x in item.split(' ')]
        x=check_safe_unsafe(nums)
        if(x==0):
          unsafes.append(nums)
        else:
            safe_total+=1
        
    print('SAFE',safe_total)
    return unsafes



def part2(list1: list[str],list2: list[str]):
#    dict1 = group_list(list1)
   dict2 = group_list(list2)
   total=0
   for x in list1:
       if(dict2.get(x)!=None):
           total+= x*dict2.get(x)
        # total+=pow(x, dict2.get(x))
    
   print(total)

def check_all(lst,index):
  newList = list(lst)
  newList.pop(index)
  
  x=check_safe_unsafe(newList)
  if(x==1):
    return 1
  else:
    if(index!=len(lst)-1):
      return check_all(lst, index+1)    
    
    
            
def solution(input: list[str]):
    unsafe_total=0
    unsafes = part1(input)
    for unsafe in unsafes:
        res=check_all(unsafe,0)
       
        if(res==1):
            unsafe_total+=1
    
    
    print('UNSAFE',unsafe_total)
        
    # part2(list1, list2)
    # print(part1(list1, list2))
   
    # print(functools.reduce(lambda a, b: int(a)+int(b), arr))

      