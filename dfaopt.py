#!/usr/bin/env python3.7
from pprint import pprint

a=[[3, 2], [4, 2], [4, 3], [5,6]]

final=[]
for i, l in enumerate(a[:-1]):
    related = []
    for el in l:
        if el in a[i+1] and el not in related:
            related.append(el)
    final.append(related)

pprint(a)
pprint(final)
