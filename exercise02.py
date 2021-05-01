heros=['spider man','thor','hulk','iron man','captain america']
heros.append('black panther')
print(len(heros))


heros.remove('black panther')
heros.insert(3, 'black panther')
print(heros)

heros[1:3] = ['doctor strange']
print(heros)

heros.sort()
print(heros)
