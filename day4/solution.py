
def score_from_range(total:int):
    if(total ==0):
        return 0;
    score=1
    for i in range(total):
        if(i==0):
            score*=1
        else:
            score*=2
    return score


def solution(input):
    sum=0
    for item in input:
        numbers = item.split(':')[1]
        winning_numbers = [e for e in numbers.split('|')[0].split(' ') if e!='']
        all_numbers = [e for e in numbers.split('|')[1].split(' ') if e!='']
        winning_dict={}
        all_dict={}
        for n in winning_numbers:
            winning_dict[n]=True
        for n in all_numbers:
            all_dict[n]=True
        total_points=0
        j=1
        for k in winning_dict:
            if(all_dict.get(k)!=None):
                    total_points+=1
                
        
        sum+=score_from_range(total_points)
            
    print(sum)