#!/usr/bin/env python3
import ipdb
def return_evens(num_list):
    ans=[]
    for i in num_list:
        if i%2==0:
            ans.append(i)
    return ans
    pass

def make_exclamation(sentence_list):
    ans=[]
    if len(sentence_list)>0:
        for sentence in sentence_list:
            ans.append(sentence[:]+"!")
        
    
    return ans