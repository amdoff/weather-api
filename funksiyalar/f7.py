def merge_alternate(list1, list2):
    list3 = []
    min_len = min(len(list1), len(list2))  
    for i in range(min_len):
        list3.append(list1[i])
        list3.append(list2[i])

    list3.extend(list1[min_len:])
    list3.extend(list2[min_len:])

    return list3

list1 = [1, 2, 3]
list2 = [11, 22, 33]
print(merge_alternate(list1, list2))  

list1 = [1, 2, 3, 4, 5]
list2 = [11, 22, 33]
print(merge_alternate(list1, list2))  

list1 = [1, 2]
list2 = [11, 22, 33, 44, 55]
print(merge_alternate(list1, list2))  
