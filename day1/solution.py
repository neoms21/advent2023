
from utils.utils import sort
def solution(input):
    arr = []
    sum=0

    for item in input:
        
        if(item!=''):
            sum+=int(item)
        else:
            arr.append(sum)
            sum=0;

    sort(arr, True)
    print(arr[0],arr[0]+arr[1]+arr[2])