
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
                x = d.strip().split()
                count = int(x[0])
                color = x[1]
                games_dict["sets"].append({"color":color, "count":count})
                # Required for part 1 and not for part 2
                if(count > colors_limit[color]):
                    allGood=False
                    break
                   
    
        if(allGood):
            sum+=int(gameId)
            
        arr.append(games_dict)    
       
    print(sum)
    
    return arr
    

def part2(input):
    gameAndSets = solution(input)
    
    sum = 0
    for g in gameAndSets:
        obj={}
        
        for s in g["sets"]:
            if(obj.get(s["color"])==None):
                obj[s["color"]]=s['count']
            elif(obj.get(s["color"])<s['count']):
                 obj[s["color"]]=s['count']
        x=1 
                
        for k in obj:
                x*=int(obj[k])
                
        sum+=x
    
    print(sum)