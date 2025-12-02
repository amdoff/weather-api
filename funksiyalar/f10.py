def swap_even_odd_values(d):
    keys = list(d.keys()) 
    for i in range(0, len(keys) - 1, 2):  
        d[keys[i]], d[keys[i + 1]] = d[keys[i + 1]], d[keys[i]]
    return d

dict1 = {1: "ABC", 2: "DEF", 3: "GHI", 4: "JKL", 5: "MNO"}

swapped_dict = swap_even_odd_values(dict1)

print(swapped_dict)
