#the same as dict but involves only keys, keys cannot be the same, is in {} and does not have order or llke in ([]), ()
#hashable - конвертация в цифровое значение, чтобы код работал быстрее, затем происходить дехеширование

# sets1 = set()
# print(sets1)

# sets2 = set('MakersCodingisEasy')
# print(sets2)

# set3 = set(['Makers', 'Coding', 'Is', 'Easy'])
# print(set3)

# set4 = set([1, 1, 1, 2, 3, 4, 5, 6, 7])
# print(set4)

# set5 = set ([1, 2, 'Makers', 4, 6 ,7, 'Coding', 'Makers'])
# print(set5)

# users = {'Bakyt', 'Ermek', 'Kanat', 'Kanat'}
# print(type(users))
# print(users)

# print(hash('Makers'))

# users = set()
# users.add(('Bakyt', 'Ermek'))
# users.add('Nellin')
# print(users)
# users.clear()
# print(users)


#####adds and makes the list unique:
# nums = set([1, 2, 3, 4, 5])
# nums2 = set([2, 3, 4, 5, 6])
# nums3 = nums.union(nums2)
# print(nums3)

#####takes only intersection:
# nums3 = nums.intersection(nums2)
# print(nums3)

# #####the item is different
# nums3 = nums.difference(nums2)
# print(nums3)
# nums3 = nums2 - nums


######issubset - имеется ли сет в другом сете
# nums = set([2, 3, 4])
# nums2 = set([2, 3, 4, 5, 6])
# print(nums2.issubset(nums))

######should contain all the elemets
#print(nums.issuperset(nums2))

##### to make the set frozen and unchangable
# users = frozenset({'Tom', 'Bob', 'Alice'})
# print(type(users))
# users.add('Sam')

# len(set)
# obj in sets1 
# obj not in sets1

# nums = set([1, 2, 3, 4])
# nums.remove(5)
# print(nums)

# nums = set([1, 2, 3, 4])
# nums.pop()
# print(nums)

# nums = set([1, 2, 3, 4])
# nums2 = set([3, 4, 5])
# nums.update(nums2)
# print(nums)

# nums = set([1, 2, 3, 4])
# nums2 = set([3, 4, 5])
# nums.discard(5)
# print(nums)















