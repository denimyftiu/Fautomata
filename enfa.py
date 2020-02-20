#!/usr/bin/env python3.7
import json
from pprint import pprint

''' 
A normal epsilon nfa.
{'alphabet': ['a', 'b', 'epsilon'],
 'hops': {'1': {'epsilon': ['1', '2', '3']},
          '2': {'a': [4], 'epsilon': []},
          '3': {'b': [5], 'epsilon': []},
          '4': {'epsilon': ['4', '6']},
          '5': {'epsilon': ['5', '6']},
          '6': {'epsilon': ['6', '7']},
          '7': {'a': [8], 'epsilon': []},
          '8': {'epsilon': ['8', '9']}},
 states': ['1', '2', '3', '4', '5', '6', '7', '8', '9']}
'''
inp =input("Isert Json file: ")
with open(inp, 'rb')as jfile:
    data = json.load(jfile)

def goes_with_epsilon(state_list):
    ret=[]
    for s in state_list:
        ret += hops[s]['epsilon'] 
    return list(set(ret))

def epsilon_closure(llist):
    ret = []
    for character in data['alphabet'][:-1]:
        cr=[]
        for state in llist:
            if character in hops[state].keys():
                cr+=hops[state][character]
        cr = goes_with_epsilon(cr)
        ret.append(cr)
    return ret


def find_endstates(state_list):
    endstates = []
    for state in state_list:
        fk = goes_with_epsilon(hops[state]['epsilon'])
        for e in data['endstate']:
            if e in fk:
                endstates.append(state)
    return endstates

if __name__=='__main__':
    hops = data['hops']
    nfa = {'alphabet': data['alphabet'][:-1],'states': data['states'],"endstate":data['endstate'], "beginstate":data['beginstate']}
    nfa_hops = {}
    for state in hops.keys():
        first_step = goes_with_epsilon(hops[state]['epsilon'])
        nfa_state = epsilon_closure(first_step)
        chars = {}
        for i,character in enumerate(nfa['alphabet']):
            chars.update({character: nfa_state[i]})
        nfa_hops.update({state : chars})
    nfa.update({"hops":nfa_hops})
    nfa['endstate'] = find_endstates(hops.keys())
    pprint(nfa)
