# -*- coding: utf-8 -*-
"""
Created on Sun Jan  2 20:52:15 2022


"""
alpha=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',\
       'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
      
def search(x):
    low=0
    high=len(alpha)-1
    while low<=high:
        mid=(low+high)//2
        if alpha[mid]<x:
            low=mid+1
        elif alpha[mid]>x:
            high=mid-1
        else:
            return mid 
    return None 
def enc(sen, key):
    res = ''
    for x in sen:
        e = search(x)
        if e is not None:
            e = e+key
            if e>=len(alpha):
                e = e-len(alpha)
            res+=alpha[e]
        else:
            res+=x
    return res
def dec(sen, key):
    res=''
    for x in sen:
        d= search(x)
        if d is not None:
            d = d-key
            res+=alpha[d]
        else:
            res+=x
    return res
def breakEnc(sen):
    import nltk
    nltk.download('words')
    from nltk.corpus import words
    for a in range(1, len(alpha)-1, 1):
        b = dec(sen, a)
        c = b.split()
        found = True
        for d in c:
            if not d in words.words():
                found = False
                break
        if found == True:
            print(c)
            print(a)
            break
    

sen='I went zoo yesterday'
enc_sen=enc(sen, 2)
print(enc_sen)        
dec_sen=dec(enc_sen, 2)
print(dec_sen) 
breakEnc(enc_sen)
   