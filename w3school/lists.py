# Исходный список
myList = [
    "lion",     # 0
    "tiger",    # 1
    "elephant", # 2
    "giraffe",  # 3
    "zebra",    # 4
    "panda",    # 5
    "wolf",     # 6
    "kangaroo", # 7
    "fox",      # 8
    "bear",     # 9
]

# 1. extend() добавляет элементы из другого списка или итерации в конец текущего списка
myList.extend(["koala", "leopard"])
print(myList)
# ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'panda', 'wolf', 'kangaroo', 'fox', 'bear', 'koala', 'leopard']

# 2. sort() сортирует список в алфавитном порядке (по умолчанию) или по ключу
myList.sort()
print(myList)
# ['bear', 'elephant', 'fox', 'giraffe', 'kangaroo', 'koala', 'leopard', 'lion', 'panda', 'tiger', 'wolf', 'zebra']

# 3. reverse() меняет порядок элементов на обратный
myList.reverse()
print(myList)
# ['zebra', 'wolf', 'tiger', 'panda', 'lion', 'leopard', 'koala', 'kangaroo', 'giraffe', 'fox', 'elephant', 'bear']

# 4. insert() вставляет элемент в указанную позицию
myList.insert(2, "dolphin")
print(myList)
# ['zebra', 'wolf', 'dolphin', 'tiger', 'panda', 'lion', 'leopard', 'koala', 'kangaroo', 'giraffe', 'fox', 'elephant', 'bear']

# 5. pop() удаляет элемент по индексу и возвращает его
removed_item = myList.pop(2)  # Удаляем элемент с индексом 2
print(removed_item)           # dolphin
print(myList)
# ['zebra', 'wolf', 'tiger', 'panda', 'lion', 'leopard', 'koala', 'kangaroo', 'giraffe', 'fox', 'elephant', 'bear']

# 6. clear() удаляет все элементы из списка
myList.clear()
print(myList)
# []

# Восстанавливаем список для дальнейших примеров
myList = [
    "lion", "tiger", "elephant", "giraffe", "zebra", 
    "panda", "wolf", "kangaroo", "fox", "bear"
]

# 7. copy() создает копию списка
copied_list = myList.copy()
print(copied_list)
# ['lion', 'tiger', 'elephant', 'giraffe', 'zebra', 'panda', 'wolf', 'kangaroo', 'fox', 'bear']

# 8. index() возвращает индекс первого вхождения указанного элемента
index_of_zebra = myList.index("zebra")
print(index_of_zebra)
# 4

# 9. remove() удаляет первое вхождение указанного элемента
myList.remove("zebra")
print(myList)
# ['lion', 'tiger', 'elephant', 'giraffe', 'panda', 'wolf', 'kangaroo', 'fox', 'bear']
