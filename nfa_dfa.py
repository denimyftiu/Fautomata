#!/usr/bin/env python3.7
import json
import sys
from pprint import pprint

with open('nfa.json', 'rb')as jfile:
    data = json.load(jfile)
'''
{"alphabet": ["a", "b"],
 "beginstate": ["A"],
 "endstate": ["B"],
 "hops": {"A": {"a": ["A", "B"], "b": ["A"]},
          "B": {"a": [], "b": []}},
 "states": ["A", "B"]
 }
'''
def union(state_list):
    ret = []
    for character in data['alphabet']:
        cr=[]
        for state in state_list:
            if character in hops[state].keys():
                cr.extend(hops[state][character])
        ret.append(sorted(cr))
    #returns the epsilon closure of a list of states 
    return ret

def put_unseen_in_stack(state_list, stack):
    for state in state_list:
        if state in seen:
            stack.append(state)
        
#pprint(data) 
hops = data['hops']
begin_state = data['beginstate']
seen= [['A']]
stack = []
#initial setup
for el in hops[begin_state[0]].values():
    if el != begin_state and el not in stack:
        stack.append(el)
        seen.append(el)

print('stack',stack)
print(max(map(len, seen)))
while len(stack) == 0:
    for i,el in enumerate(stack):
        newstates = union(el)     
        put_unseen_in_stack(newstates, stack)
        stack.pop(i)
    print('new',newstates)
    print('seen',seen)
    print('stack',stack)
