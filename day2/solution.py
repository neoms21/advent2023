
from utils.utils import sort
import functools

colors_limit= {'red':12, 'green':13,'blue':14}
def solution(input):
    arr = []
    
    sum=0
    for i in input:
        x = i.split(':')
        gameId = x[0].split(' ')[1]
        sets= x[1].split(';')
        games_dict={"sets":[], "gameId": gameId}
        allGood = True
    
        for s in sets:
            draws = s.split(',')
           
            for d in draws:
                x = d.strip().split(' ')
                count = int(x[0])
                color = x[1]
                if(count > colors_limit[color]):
                    allGood=False
                    break
                    
                #     break
                # else:
                #    games_dict["gameId"]["sets"].append({color:count})
    
        if(allGood):
            sum+=int(gameId)
            
        arr.append(games_dict)    
       
    print(sum)
    

def part2(input):
    x=10