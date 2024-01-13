# list_a = [1,2,3,4,5]

# list_b = list_a

# list_b.append(6)

# print(list_a)

# print(id(list_a))
# print(id(list_b))

# --------------------------------------------------------
# 얕은 복사
# list_a = [1,2,3]
# list_b = list_a.copy()

# list_b.append(4)

# print(f"list_a : {list_a}")
# print(f"list_b : {list_b}")

# print(f"id of list_a : {id(list_a)}")
# print(f"id of list_b : {id(list_b)}")

# --------------------------------------------------------
# 깊은 복사
from copy import deepcopy

list_a = [1,2,3,4,[5,6]]
list_b = deepcopy(list_a)

list_b[4].append(7)

print(f"list_a : {list_a}")
print(f"list_b : {list_b}")

print(f"id of list_a : {id(list_a)}")
print(f"id of list_b : {id(list_b)}")

# --------------------------------------------------------
