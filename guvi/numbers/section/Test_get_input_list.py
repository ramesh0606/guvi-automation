# print("get elements length:")
elements_length = int(input())
print(elements_length)
# print("you can enter ",elements_length , "numbers by pressing enter after each number")
new_list = []
for x in range(elements_length):
    new_list.append(input())

print(new_list)
