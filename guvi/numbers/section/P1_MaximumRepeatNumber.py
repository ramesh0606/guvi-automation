# print("get elements length:")
elements_length = input()
# print("get elements length:",elements_length)
# print("you can enter ",elements_length , "numbers by pressing enter after each number")
numbers_list = []
for x in range(int(elements_length)):
    numbers_list.append(input())
print(numbers_list)
# = [1,2,3,4,4,4,5]
# print("numbers_list",numbers_list)
m = {}
for x in numbers_list:
    if m.setdefault(x):
        m[x] = m.setdefault(x) + 1
    else:
        m[x] = 1
# print("m map is :", m)
# Think to find which key repeats more times
key_list = list(m)
# key_list = [1,2,3,4,5]
# print("key_list:", key_list[0])
temp_key = key_list[0]  # temp_key = 1 , 4
for key in key_list[1:]:  # 1, 2, 3
    if m.setdefault(temp_key) == m.setdefault(key):  # 1 == 1
        continue
    elif m.setdefault(temp_key) < m.setdefault(key):  # 1 <= 1
        temp_key = key
print(temp_key)
