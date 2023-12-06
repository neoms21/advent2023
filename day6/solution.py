def solution(input):
    inputs = [
        (45988373,295173412781210)
    ]
    x = (1,0)
    result = 1
    for input in inputs:
        upper=input[0]
        limit=input[1]
    
        total = 0
        for i in (range(1,upper)):
            if((upper-i)*i>limit):
                total+=1
        result*=total
    print(result)