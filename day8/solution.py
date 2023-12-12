direction_map={
    'L':0,
    'R':1
}
directions=''
result_found = False
first_key = 'AAA'
def solution(input):

    resultant_key ='ZZZ'
    nodes = {}
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
            
    # print(nodes)
    global result_found
    global first_key
    runs = 0
    while(result_found!=True):
        for d in directions:
            runs+=1
            tuple_index = direction_map[d]
            # print(f"Before==>> node_key: {first_key} - {d}")
            first_key = nodes[first_key][tuple_index]
            print(f"After==>> node_key: {first_key} - {d}")
            if(first_key== resultant_key):
                break
           
        print(runs,{first_key})
        if(first_key==resultant_key):
            result_found=True
    
    print(f'Total iterations={runs}')
            