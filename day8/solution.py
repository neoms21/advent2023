
from itertools import cycle
import re
import math

direction_map={
    'L':0,
    'R':1
}
with open('day8/input.txt', 'r') as f:
    puzzle_input = f.read()
          
def part1(nodes, directions, first_key='AAA'):
   
    result_found = False
    
    runs = 0
    while(result_found!=True):
        for d in directions:
            runs+=1
            tuple_index = direction_map[d]
            first_key = nodes[first_key][tuple_index]
            if(first_key[2]=='Z'):
                break
           
        if(first_key[2]=='Z'):
            result_found=True
    
    print(f'Total iterations = {runs}')
    return runs


def is_final_nodes(nodes):
    filtered_nodes = [n for n in list(nodes) if n[2]=='Z']
    return len(filtered_nodes)==2

def part2(nodes, directions):
    runs = []
    starting_nodes = [n for n in list(nodes.keys()) if n[2]=='A']
    
    for n in starting_nodes:
        r = part1(nodes,directions,n)
        runs.append(r)
       
       
    print(math.lcm(*runs))
    
    
def part2_gh(puzzle_input):
    directions, connections = puzzle_input.split('\n\n')
    directions = [0 if d == 'L' else 1 for d in directions]
    graph = {}
    regex = r'(\w{3}) = \((\w{3}), (\w{3})\)'
    for node, left, right in re.findall(regex, connections):
        graph[node] = [left, right]

    starting_nodes = [node for node in graph if node[2] == 'A']
    cycles = []
    for node in starting_nodes:
        for steps, d in enumerate(cycle(directions), start=1):
            node = graph[node][d]
            if node[2] == 'Z':
                cycles.append(steps)
                break

    print(f"==>> cycles: {cycles}")
    return math.lcm(*cycles)

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
     part2(nodes, directions)
    #  print(part2_gh(puzzle_input))
  