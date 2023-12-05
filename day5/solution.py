

from utils.utils import map_to_int

maps = []
def create_map_tuples(first:str, second:str, arr ):
    result = {first:[], second:[]}
    for i,a in enumerate(arr):
        nums = list(map(map_to_int,a.split(' ')))
        lower = nums[0]
        upper = nums[1]
        rng = nums[2]
        result[first].append((upper, upper+rng-1))
        result[second].append((lower, lower+rng-1))
    maps.append(result)

def solution(input:[str]):
    locations =[]
    seeds =[]
    lines = []
    next_is_map = False
    first = ''
    second = ''
    for idx,line in enumerate(input):
        
        if(line.find('seeds')==0):
            seeds =  list(map( map_to_int, list(filter(None, line.split(':')[1].split(' ')))))
            continue
        if(line.find('map:')!=-1):
              next_is_map = True
              x = line.split(' ')[0].split('-to-')
              first= x[0]
              second= x[1]
             
              
              continue
        if(next_is_map == True and line!=''):
            lines.append(line)
        if((line == '' or idx == len(input)-1) and next_is_map == True):
           next_is_map = False
           create_map_tuples(first,second,lines)
           lines=[]
           
    print(seeds)
    def find_matching_map_id(dct, num):
    
        keys = list(dct.keys())
        key1 = keys[0]
        key2 = keys[1]
        soil_location=num
        for i,first_tup in enumerate(dct[key1]):
            second_tup = dct[key2][i]
            # if(num==52):
            #     print(num, first_tup,second_tup)
            if(num>=first_tup[0] and num<=first_tup[1]):
                soil_location= second_tup[0]+ num- first_tup[0]
                # print(f"==>> key1: {key1}{key2}{soil_location}")
        # print(f"==>> soil_location: {key1}{key2}{soil_location}")
        return soil_location
        
    for seed in seeds:
        x=seed
        for farm_map in maps:
            y=x
            y= find_matching_map_id(farm_map, y)
            if(y==None):
                y=x
            else:
                x=y
        locations.append(x)
    locations.sort()
    
    print(locations[0])