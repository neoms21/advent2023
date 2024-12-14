
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

def get_points(item:str):
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
        
    return total_points    

cards = []

    

part2Total = 0 
def recursion(next_cards_count,index, input):
        global part2Total       
        if(next_cards_count>0):
            i = index+1
            while i < next_cards_count+index+1:
                next_cards = get_points(input[i])
                part2Total+=next_cards
                if(next_cards):
                    recursion(next_cards,i,input)
                i += 1
                
   
def part2(input):
    global part2Total
    for index,item in enumerate(input):
        print(f"==>> item: {item}")
        
        part2Total+=1
        next_cards_count = get_points(item)
        part2Total+=next_cards_count
        recursion(next_cards_count, index, input)
        
           
        
            
    
    print(f"==>> part2Total: {part2Total}")