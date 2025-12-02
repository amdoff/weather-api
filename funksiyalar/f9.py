def merge_lists(keys, names, values):
    result = [{k: {n: v}} for k, n, v in zip(keys, names, values)]
    return result

keys = ['S001', 'S002', 'S003', 'S004']
names = ['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
values = [85, 98, 89, 92]

merged_list = merge_lists(keys, names, values)
print(merged_list)
