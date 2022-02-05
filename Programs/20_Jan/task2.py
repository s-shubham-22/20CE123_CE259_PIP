# 1.
# Flatten the following list of lists of lists to a one dimensional list :
# list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
# output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

nestedList = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
element = 0
print(f"1: \n{[item for sublist in nestedList for item in sublist]}")
print('')

# 2.
# Using list comprehension create the following list of tuples:
# [(0, 1, 0, 0, 0, 0, 0),
# (1, 1, 1, 1, 1, 1, 1),
# (2, 1, 2, 4, 8, 16, 32),
# (3, 1, 3, 9, 27, 81, 243),
# (4, 1, 4, 16, 64, 256, 1024),
# (5, 1, 5, 25, 125, 625, 3125),
# (6, 1, 6, 36, 216, 1296, 7776),
# (7, 1, 7, 49, 343, 2401, 16807),
# (8, 1, 8, 64, 512, 4096, 32768),
# (9, 1, 9, 81, 729, 6561, 59049),
# (10, 1, 10, 100, 1000, 10000, 100000)]

li = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ans = []
print('2:')
print(*(ele for ele in [(num, num**0, num**1, num**2, num**3, num**4, num**5) for num in li]), sep='\n')

# Flatten the following list to a new list:
# countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output:
# [['FINLAND','FIN', 'HELSINKI'], ['SWEDEN', 'SWE', 'STOCKHOLM'], ['NORWAY', 'NOR', 'OSLO']]
print('\n3:')
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
ans = [li for li in [[ele[0].upper(), ele[0][0:3].upper(), ele[1].upper()] for nli in countries for ele in nli]]
print(*ans, sep='\n')

# 4. Change the following list to a list of dictionaries:
# countries = [[('India', 'Delhi')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
# output: [{'country': 'India', 'city': 'Delhi'},
# {'country': 'SWEDEN', 'city': 'STOCKHOLM'},
# {'country': 'NORWAY', 'city': 'OSLO'}]

print('\n4:')
countries = [[('India', 'Delhi')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
ans = [li for li in [{'country': ele[0], 'city': ele[1]} for nli in countries for ele in nli]]
print(*ans, sep='\n')

# 5. Change the following list of lists to a list of concatenated strings:
# names = [[('Mrugendra', 'Rahevar')], [('Martin', 'Parmar')], [('Chintan', 'Vyas')], [('Nikunj', 'Patel')]]
# output: ['Mrugendra Rahevar', 'Martin Parmar', 'Chintan Vyas', 'Nikunj Patel']

print('\n5:')
names = [[('Mrugendra', 'Rahevar')], [('Martin', 'Parmar')], [('Chintan', 'Vyas')], [('Nikunj', 'Patel')]]
ans = [ele[0] + ' ' + ele[1] for nli in names for ele in nli]
print(*ans, sep='\n')
