a = [(1, 2), (5, 1), (0, 1), (5, 2), (3, 0)]

c = sorted(a, key = lambda x : x[0]) 
print(c)

c = [(0, 1), (1, 2), (3, 0), (5, 1), (5, 2)]
print(c)

arr = ['abc', 'bac', 'bca']
re = sorted(arr, key=lambda x : x[1])
print(re)


b = [12, 14, 23, 24, 16]
print(range(len(b)))
b_idx = sorted(range(len(b)), key = lambda k: b[k]) 
print(b_idx)