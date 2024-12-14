import itertools

import pprint
card_map = {
        "A":14, 
        "K":13,
        "Q":12,
        "J":1,
        "T":10,
        "9":9,
        "8":8,
        "7":7, 
        "6":6, 
        "5":5, 
        "4":4, 
        "3":3, 
        "2":2
    }


def get_hand_type(hand:dict):
    vals = list(hand.values())
    if(vals.count(5)==1):
        return 0 #five
    elif(vals.count(4)!=0):
       return 1 #four
    elif(vals.count(3)!=0 and vals.count(2)!=0):
       return 2 #full house
    elif(vals.count(3)!=0):
       return 3 #three
    elif(vals.count(2)==2):
       return 4 #2 pair
    elif(vals.count(2)==1):
       return 5 #1 pair
    else:
       return 6 #all unique
   
def get_hand_type_2(hand:dict, card):
    
    vals = list(hand.values())
    if(hand.get("J")==None):
        if(vals.count(5)==1):
            return 0 #five
        elif(vals.count(4)!=0 ):
            return 1 #four
        elif(vals.count(3)!=0 and vals.count(2)!=0):
            return 2 #full house
        elif(vals.count(3)!=0):
            return 3 #three
        elif(vals.count(2)==2):
            return 4 #2 pair
        elif(vals.count(2)==1):
            return 5 #1 pair
        else:
            return 6 #all unique - high card
    else:
        joker_count = hand["J"]
        if(vals.count(5)==1):
            return 0 #five
        elif(vals.count(4)!=0):
            if(joker_count >0):
               return 0
        elif(vals.count(3)!=0):
            print(card)
            if(joker_count ==3):
               return 1
            if(joker_count ==2):
                return 0
            if(joker_count ==1):
                return 1
            return 2 #full house
       
        elif(vals.count(2)==2):
           
            if(joker_count ==3):
               return 0
            if(joker_count ==2):
                return 1
            if(joker_count ==1):
                return 2
        elif(vals.count(2)==1):
             if(joker_count ==3):
               return 0
             if(joker_count ==2):
                return 3
             if(joker_count ==1):
                return 3
        else:
            if(joker_count ==1):
                return 5
            return 6 #all unique - high card
    return 0
        
        
def myFunc(e):
  return e['kind']    

def solution(input):
    dct = {}
    hands = []
    for item in input:
        hand_str,bid = item.split(' ')
        hand = {"card":hand_str, "dct":{},"card_values":[], "bid":int(bid)}
        dct={}
        for i in hand_str:
            hand["card_values"].append(card_map.get(i))
            if(dct.get(i)==None):
                dct[i] = 1
            else:
                dct[i]+=1
            hand["dct"] =dct
        
        hand["kind"] = get_hand_type_2(hand['dct'], hand["card"])
       
        hands.append(hand)
    hands.sort(reverse=True,key=myFunc)
    result = []
    rank=0
    
    
    for key, igroup in itertools.groupby(hands, lambda x: x["kind"] ):
        grouped_list = list(igroup)
        
        
        if(len(grouped_list)>1):
            grouped_list.sort(key=lambda h: (h["card_values"]))
            for gl in grouped_list:
                rank+=1
                gl['rank']=rank
                result.append(gl)
        else:
            rank+=1
            
            grouped_list[0]['rank'] = rank
            result.append(grouped_list[0])
    
    total = 0
    
    for r in result:
        print(f"==>> r: {r['card']} - {r['rank']} - {r['kind']}")
        total+=r['rank']*r['bid']
    print(total)
