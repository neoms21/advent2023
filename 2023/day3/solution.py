from utils.utils import has_special_char

special_chars=[]
astericks = {}
part2Numbers = []
def filter_numbers_list(item):
    print(f"==>> item: {item}")
    if(item["rowId"]==0 or item["rowId"]== 1):
        return True

    return False
    
     #                       "neighboursT":[
        # (x-1,y),
        # (x+1,y),
        # (x,y-1),
        # (x,y+1),
        # (x+1,y+1),
        # (x-1,y+1),
        # (x-1,y-1),
        # (x+1,y-1),
    # ],

    
def add_neighbours_coords(x:int,y:int, ch:str):
    special_chars.append({
    "rowId":x,
    "own":ch, 
    "neighbours": {
        f"{x-1}{y}":True,
        f"{x+1}{y}":True,
        f"{x}{y-1}":True,
        f"{x}{y+1}":True,
        f"{x+1}{y+1}":True,
        f"{x-1}{y+1}":True,
        f"{x-1}{y-1}":True,
        f"{x+1}{y-1}":True,                     
    }})
   
def solution(input):
    total = 0
    part2Total = 0
    numbers_list= []
    num=''
    num_coordinates = {}
 
    for i, value in enumerate(input):
        
        for j,v in enumerate(value):
            if(v.isnumeric()):
               num+=v
               num_coordinates[f"{i}{j}"] = True
            elif(v=='.'):
               if(len(num))>0:
                   numbers_list.append({"rowId":i,"value":int(num),"coordinates":num_coordinates})
                   num=''
                   num_coordinates= {}
            elif(has_special_char(v)):
                add_neighbours_coords(i,j,v)
                if(len(num))>0:
                   numbers_list.append({"rowId":i,"value":int(num),"coordinates":num_coordinates})
                   num=''
                   num_coordinates= {}
    
    
    print(len(numbers_list), len(special_chars))
    for sc in special_chars:
        rowIndex=int(sc["rowId"])
        filtered_list = [e for e in numbers_list if e['rowId'] == rowIndex or  e['rowId'] == rowIndex-1 or  e['rowId'] == rowIndex+1 ]
        for f in filtered_list:
            for c in f["coordinates"]:
                if(sc["neighbours"].get(c)!=None):
                    if(sc["own"]=='*'):
                        if(astericks.get(sc["rowId"]) != None and astericks[sc["rowId"]]["neighbours"] == sc["neighbours"]):
                            part2Numbers.append(f["value"])
                            part2Total+=astericks[sc["rowId"]]["value"]*f["value"]
                            astericks[sc["rowId"]] = None
                        else:
                            astericks[sc["rowId"]] = {"value":f["value"], "neighbours": sc["neighbours"]}
                    total+=f["value"]
                    break


    print(total)
    print(part2Total)                        
                          