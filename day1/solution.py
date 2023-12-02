
from utils.utils import sort
import functools

numbers = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

def findNumber(item:str):

    num= ''
    for i in item:
       
        if (i.isnumeric()):
            num += i
            break

    for i in (item[::-1]):
        if (i.isnumeric()):
            num += i
            break
        
    return num

def solution(input):
    arr = []
    
    for item in input:
        num = ''    
        arr.append(num)

    # print(functools.reduce(lambda a, b: int(a)+int(b), arr))


def replaceWords(input:str):
   out=''
   res=''
   for i in input:
       if(i.isnumeric()):
           res+=i
           break
       out+=i
       for key in numbers.keys():
           if(out.find(key)!=-1):
              
               res+=numbers[key]
               out=''
               break
       if(out==''):
           break
        
   
   for i in input[::-1]:
       if(i.isnumeric()):
           res+=i
           break
       out+=i
      
       for key in numbers.keys():
           if(out.find(key[::-1])!=-1):
              
               res+=numbers[key]
               out=''
               break
       if(out==''):
           break  
   return res

        
def part2(items):
    arr = []
    
    for input in items:
        value=''
        
        converted = replaceWords(input)
        value = findNumber(converted)
        arr.append(value)
    
    print(functools.reduce(lambda a, b: int(a)+int(b), arr))