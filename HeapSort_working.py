# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 09:43:54 2019

@author: maryn
"""
A = [29, 7, 89, 16, 33, 111, 67, 6, 9, 25, 29, 120, 59, 268, 2, 5, 19, 8, 1, 10]
#heapsizeA = 6

def parent(i):
    parent = i//2
    #print('parent', parent)
    return(parent)

def left(i):
    left = i*2+1
    #print('i=,', i, 'left from function', left)
    return(left)

def right(i):
    right = 2*i+2
    #print('i=', i, 'right from function', right)
    return(right)

def maks_heapify(A,i):
    #heapsizeA = len(A)
    l = left(i)
    r = right(i)
    #print('left=', l, 'right=', r)
    #print('heapsizeA=',heapsizeA)
    if l <= heapsizeA and A[l] > A[i]:
        largest = l
        #print('l-largest', largest)
    else: largest = i
    if r <= heapsizeA and A[r] > A[largest]:
        largest = r
        #print('r-largest', largest)
    if largest != i:
        #print('A[largest]=', A[largest])
        A[i], A[largest] = A[largest], A[i]
        #print(A)
        maks_heapify(A, largest)

def build_maks_heap(A):
    global heapsizeA
    heapsizeA = len(A)-1
    for i in range(len(A)//2, -1, -1):
        #print('i=', i)
        maks_heapify(A,i)
        
def heap_sort(A):
    build_maks_heap(A)
    for i in range(len(A)-1, 0, -1):
        A[0], A[i] = A[i], A[0]
        #print('last one', A[i], 'first one', A[0])
        #print('after cutting the largest element i=', i)
        #print(heapsizeA)
        global heapsizeA
        heapsizeA -= 1
        maks_heapify(A,0)
        
heap_sort(A)
print('sorted:', A)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    