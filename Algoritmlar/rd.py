from random import randint as rd
def quick_sort(items:list)->list:
    low,mid,high,= [],[],[]
    for i in range(0,1000):
        if items < mid:
            low.append(low)
        elif items > mid:
