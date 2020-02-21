#!/usr/bin/env python3.7
import json
import sys
from pprint import pprint

def union(state_list):
    ret = []
    for character in data['alphabet']:
        cr=[]
        for state in state_list:
            cr.extend(hops[state][character])
        ret.append(sorted(cr))
    return ret

def find_final_states(seen):
    final_states = []
    for el in seen:
        if final_state in el:
            final_states.append(''.join(el))
    return final_states

def update_stack(newstates, stack, seen):
    for state in newstates:
        if state not in stack and state not in seen:
            stack.append(sorted(state))
            seen.append(sorted(state))

if __name__=='__main__':
    #take the filename as argument
    try:
        inp = sys.argv[1]
    except:
        print('No File Input')
        exit(1)

    with open(inp, 'rb')as jfile:
        data = json.load(jfile)

    hops = data['hops']
    begin_state = data['beginstate']
    final_state = data['endstate'][0]
    seen= []
    stack = []
    stack.append(begin_state)
    seen.append(begin_state)

    dfa = {'alphabet':data['alphabet'],'states': data['states'],
        "beginstate":data['beginstate']}
    dfa_hops = {}

    while len(stack) > 0:
        print('before pop {}'.format(stack))
        newstates = union(stack[0])     
        update_stack(newstates, stack, seen)
        chars = {}
        el = stack.pop(0)
        print('after pop {}'.format(stack))
        for i,character in enumerate(data['alphabet']):
            chars.update({character: ''.join(newstates[i])})
        dfa_hops.update({''.join(el):chars})

    final_states = find_final_states(seen)
    dfa['endstate']=final_states
    dfa['hops']=dfa_hops
    pprint(dfa)
