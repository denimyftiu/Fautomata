#!/usr/bin/env python3.7
import json
import sys
from pprint import pprint

def goes_with_epsilon(state_list):
    ret=[]
    for s in state_list:
        #join dhe jumps with epsilon
        ret += hops[s]['epsilon'] 
    #returns a list of where the state can go with epsilon
    return list(set(ret))

def epsilon_closure(state_list):
    ret = []
    #where are we going with each character in the alphabet
    for character in data['alphabet'][:-1]:
        cr=[]
        #do that for every state in the given list
        for state in state_list:
            if character in hops[state].keys():
                cr+=hops[state][character]
        cr = goes_with_epsilon(cr)
        ret.append(cr)
    #returns the epsilon closure of a list of states 
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
    #take the filename as argument
    inp = sys.argv[1]

    with open(inp, 'rb')as jfile:
        data = json.load(jfile)

    #we only need the hops dictionary for the algorithm
    hops = data['hops']
    #prepare the json for the nfa
    nfa = {'alphabet': data['alphabet'][:-1],'states': data['states'],
            "endstate":data['endstate'], "beginstate":data['beginstate']}
    nfa_hops = {}

    #runs the algorithm for the given json e-nfa
    for state in hops.keys():
        first_step = goes_with_epsilon(hops[state]['epsilon'])
        nfa_state = epsilon_closure(first_step)
        chars = {}
        for i,character in enumerate(nfa['alphabet']):
            chars.update({character: nfa_state[i]})
        nfa_hops.update({state : chars})

    #print the nfa for later use
    nfa.update({"hops":nfa_hops})
    nfa['endstate'] = find_endstates(hops.keys())
    pprint(nfa)
