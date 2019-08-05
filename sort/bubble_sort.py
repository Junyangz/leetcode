import timeit

# O(n2)
# recursion take more time
# not better
def bubble_sort(unsorted):
    if len(unsorted) < 2:
        return unsorted
    for i in range(len(unsorted) - 1):
        if unsorted[i] > unsorted[i+1]:
            unsorted[i], unsorted[i+1] = unsorted[i+1], unsorted[i]
    return bubble_sort(unsorted[:-1]) + [unsorted[-1]]

# @Python algorithm
def bubble_sort_v2(unsorted):
    length = len(unsorted)
    for i in range(length-1):
        swapped = False
        for j in range(length-1-i):
            if unsorted[j] > unsorted[j+1]:
                swapped = True
                unsorted[j], unsorted[j+1] = unsorted[j+1], unsorted[j]
        if not swapped: break  # Stop iteration if the unsorted is sorted.
    return unsorted

def bubble_sort_time(): 
    SETUP_CODE = ''' 
from __main__ import bubble_sort
from random import randint'''
  
    TEST_CODE = ''' 
mylist = [x for x in range(100)] 
bubble_sort(unsorted = mylist)'''
      
    # timeit.repeat statement 
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 1000) 
  
    # priniting minimum exec. time 
    print('Bubble sort time: {}'.format(min(times))) 

def bubble_sort_v2_time(): 
    SETUP_CODE = ''' 
from __main__ import bubble_sort_v2
from random import randint'''
  
    TEST_CODE = ''' 
mylist = [x for x in range(100)] 
bubble_sort_v2(unsorted = mylist)'''
      
    # timeit.repeat statement 
    times = timeit.repeat(setup = SETUP_CODE, 
                          stmt = TEST_CODE, 
                          repeat = 3, 
                          number = 1000) 
  
    # priniting minimum exec. time 
    print('Bubble sort time: {}'.format(min(times))) 

bubble_sort_time()
bubble_sort_v2_time()