direction_map={
    'L':0,
    'R':1
}
          
def part1(nodes, directions):
    resultant_key ='ZZZ'
   
    result_found = False
    first_key = 'DTA'
    
    runs = 0
    while(result_found!=True):
        for d in directions:
            runs+=1
            tuple_index = direction_map[d]
            # print(f"Before==>> node_key: {first_key} - {d}")
            first_key = nodes[first_key][tuple_index]
            # print(f"After==>> node_key: {first_key} - {d}")
            if(first_key== resultant_key):
                break
           
        if(first_key[2]=='Z'):
            result_found=True
    
    print(f'Total iterations = {runs}')


def is_final_nodes(nodes):
    filtered_nodes = [n for n in list(nodes) if n[2]=='Z']
    return len(filtered_nodes)==len(nodes)

def part2(nodes, directions):
    result_found = False
    runs = 0
    starting_nodes = [n for n in list(nodes.keys()) if n[2]=='A']
    print(f"==>> starting_nodes: {starting_nodes}")
    
    next_nodes = []
    while(result_found!=True):
        for d in directions:
            for n in starting_nodes:
                tuple_index = direction_map[d]
                next_nodes.append(nodes[n][tuple_index])
            starting_nodes = next_nodes
            print(f"==>> starting_nodes: {starting_nodes}")
            next_nodes=[]
            runs+=1
            # print(runs)
       
        if(runs>100 or is_final_nodes(starting_nodes)==True):
            result_found= True
            
    print(runs)
def solution(input):
     nodes = {}
     directions=''
     for i, item in enumerate(input):
        if(i==0):
            directions=item
        elif(i==1):
            continue
        else:    
            s1 = item.split(' = ')
            key = s1[0]
            val= s1[1]
            
            y=val.replace("(","").replace(')',"").split(', ')
            nodes[key] = (y[0],y[1])
    
     part1(nodes, directions)
    #  part2(nodes, directions)
  