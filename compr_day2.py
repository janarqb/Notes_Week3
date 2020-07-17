#range это функция которая дает нам диапозон, дает атрибут для старта, конца 
#comp - генератор списков, упрощенный список, быстрее
# num = range(10)
# print(type(num))
# list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# nums1 = []
# for a in nums:
#     nums1.append(a)

# nums2 = [i for i in nums]

# print(nums1, nums2)

# nums = [i**2 for i in range(5)]
# print(nums)

# list1 = list(range(1, 30))
# list2 = [num for num in list1 if num % 2 == 0]
# print(list2)

# list1 = [-30, 0, 2, 6, 11, 54, 29. -5]
# list2 = [num for num in list1 if num%2 == 0 and num > 0]
# print(list2)

# words = ['2020', '2012', '2031year', 'stroka']
# list1 = [word for word in words if word.isdigit()]
# print(list1)

# nums =
# new_list = [len(num) for num in nums]
# print(new_list)

# list1 = [-5, -12, 0, 1, 2, 8, 4, 5, 7]
# list2 = [num if num < 0 else num**2 for num in list1]
# print(list2)

# names = ['Bakyt', 'John', 'Abdukerim', 'Mekhmet', 'Ainura', 'Sooranbay', 'Sharip', 'Atanbay', 'Kut', 'Andumalik']
# filtered_names = [name + ' ' + 'bigger' if len(name) >= 6 else name + ' ' +'smaller' for name in names]
# print(filtered_names)

# John = {'name': 'John', 'age': '22'}
# Sam = {'name':'Sam', 'age':'23'}
# Peter = {'name': 'Peter', 'age': '17'}

# users = [John, Sam, Peter] 

# ages = [user['age'] for user in users]
# print(ages)

# matrix = [ 
#     [0, 1, 2, 3],
#     [10, 11, 12],
#     [20, 21, 22], 
#     [30, 31, 32]
# ]

# new_list = [x for row in matrix for x in row]
# print(new_list)

# from datetime import datetime

# start = datetime.now()

# # list_ = []
# # for i in range (10**5):
# #     list_.append(i)
# list_ = {x for x in range(10**10)}
# print(datetime.now()-start)


